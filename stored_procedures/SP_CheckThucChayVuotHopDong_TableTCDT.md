# Stored Procedure: `CheckThucChayVuotHopDong_TableTCDT`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2018-08-08 14:39:07.360000
- **Ngày sửa cuối**: 2025-12-05 10:54:06.460000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@FromDate` | `datetime(8)` | No |
| `@ToDate` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:       <Author,,Name>
-- Create date:  <Create Date,,>
-- Description:  <Description,,>
-- =============================================

-- EXEC CheckThucChayVuotHopDong_TableTCDT '2019-12-05','2019-12-05'
CREATE PROCEDURE [dbo].[CheckThucChayVuotHopDong_TableTCDT]
    @FromDate DATETIME,
    @ToDate   DATETIME
AS
BEGIN
    SET NOCOUNT ON;

    ------------------------------------------------------------
    -- 0. Tạo lại bảng hợp đồng nguồn
    ------------------------------------------------------------
    EXEC CheckThucChayVuotHopDong_TableHopDong;

    /*
    -- Tham khảo cấu trúc (đã được tạo sẵn ngoài proc)
    -- CREATE TABLE KS_ThucChay_TCDT
    -- (
    --     SoHopDong         NVARCHAR(50),
    --     Nam               INT,
    --     HopDongID         INT,
    --     HopDongChiTietID  INT,
    --     NgayThucHien      DATETIME,
    --     DmHinhThucQuangCao INT,
    --     DmLoaiBannerREF   INT,
    --     DmSanPhamREF      INT,
    --     SoLuongThucChay   FLOAT,
    --     DonViTinh         NVARCHAR(50),
    --     ThanhTienThucChay FLOAT,
    --     ThanhTienThucChayKM FLOAT
    -- )
    */

    ------------------------------------------------------------
    -- 1. KS_ThucChay_TCDT (ThucChayDaTinh & ThucChayDaTinhAdmarket)
    ------------------------------------------------------------

    -- Xóa dữ liệu cũ trong khoảng ngày để nạp lại
    DELETE FROM KS_ThucChay_TCDT
    WHERE NgayThucHien BETWEEN @FromDate AND @ToDate;

    ------------------- ThucChayDaTinh --------------------
    INSERT INTO KS_ThucChay_TCDT
    SELECT  SoHopDong,
            Nam,
            HopDongID,
            HopDongChiTietREF,
            NgayThucHien,
            DmHinhThucQuangCao,
            DmLoaiBannerREF,
            DmSanPhamREF,
            SUM(ISNULL(SoLuongThucChay + SoLuongThayDoi, 0))                    AS SoLuongThucChay,
            DonViTinh,
            SUM(ISNULL(ThanhTienSauTrietKhauThucChay, 0) + ISNULL(GiaTriThayDoi, 0)) AS ThanhTienThucChay,
            SUM(ISNULL(ThanhTienKM, 0) + ISNULL(GiaTriKMThayDoi, 0))            AS ThanhTienThucChayKM,
            GETDATE()   -- cột thêm sau (LastModifiedAt / NgayChay, tuỳ schema thực tế)
    FROM dbo.ThucChayDaTinh
    WHERE TrangThaiHopDong <> 3
      AND NgayThucHien BETWEEN @FromDate AND @ToDate
      AND DmSanPhamREF NOT IN (585, 144, 628, 337, 299)
      AND HopDongID <> 0
      AND Nam >= 2015
      -- AND DmChienDichREF = 0 -- không lấy GG/Facebook (nếu cần thì mở lại)
    GROUP BY SoHopDong,
             Nam,
             HopDongID,
             HopDongChiTietREF,
             NgayThucHien,
             DmHinhThucQuangCao,
             DmLoaiBannerREF,
             DmSanPhamREF,
             DonViTinh;

    ------------------- ThucChayDaTinhAdmarket --------------------
    INSERT INTO KS_ThucChay_TCDT
    SELECT  SoHopDong,
            Nam,
            HopDongID,
            HopDongChiTietREF,
            NgayThucHien,
            DmHinhThucQuangCao,
            DmLoaiBannerREF,
            DmSanPhamREF,
            SUM(ISNULL(SoLuongThucChay, 0))                                       AS SoLuongThucChay,
            DonViTinh,
            SUM(ISNULL(ThanhTienSauTrietKhauThucChay, 0) + ISNULL(GiaTriThayDoi, 0)) AS ThanhTienThucChay,
            SUM(ISNULL(ThanhTienKM, 0) + ISNULL(GiaTriKMThayDoi, 0))             AS ThanhTienThucChayKM,
            GETDATE()
    FROM dbo.ThucChayDaTinhAdmarket
    WHERE TrangThaiHopDong <> 3
      AND NgayThucHien BETWEEN @FromDate AND @ToDate
      AND DmSanPhamREF IN (585, 144, 628, 337, 299)
      AND HopDongID <> 0
      AND Nam >= 2015
    GROUP BY SoHopDong,
             Nam,
             HopDongID,
             HopDongChiTietREF,
             NgayThucHien,
             DmHinhThucQuangCao,
             DmLoaiBannerREF,
             DmSanPhamREF,
             DonViTinh;

    ------------------------------------------------------------
    -- 2. KS_ThucChay_TCDT_Inventory
    ------------------------------------------------------------

    /*
    -- CREATE TABLE KS_ThucChay_TCDT_Inventory
    -- (
    --     SoHopDong         NVARCHAR(50),
    --     Nam               INT,
    --     HopDongID         INT,
    --     HopDongChiTietID  INT,
    --     NgayThucHien      DATETIME,
    --     DmHinhThucQuangCao INT,
    --     DmLoaiBannerREF   INT,
    --     DmSanPhamREF      INT,
    --     SoLuongThucChay   FLOAT,
    --     DonViTinh         NVARCHAR(50),
    --     ThanhTienThucChay FLOAT,
    --     ThanhTienThucChayKM FLOAT
    -- )
    */

    -- Xóa dữ liệu cũ trong khoảng ngày để nạp lại
    DELETE FROM KS_ThucChay_TCDT_Inventory
    WHERE NgayThucHien BETWEEN @FromDate AND @ToDate;

    ------------------- ThucChayDaTinh -> Inventory --------------------
    INSERT INTO KS_ThucChay_TCDT_Inventory
    SELECT  SoHopDong,
            Nam,
            HopDongID,
            HopDongChiTietREF,
            NgayThucHien,
            DmHinhThucQuangCao,
            DmLoaiBannerREF,
            DmSanPhamREF,
            SUM(ISNULL(SoLuongThucChay, 0))                                      AS SoLuongThucChay,
            DonViTinh,
            SUM(ISNULL(ThanhTienSauTrietKhauThucChay, 0) + ISNULL(GiaTriThayDoi, 0)) AS ThanhTienThucChay,
            SUM(ISNULL(ThanhTienKM, 0) + ISNULL(GiaTriKMThayDoi, 0))             AS ThanhTienThucChayKM
    FROM dbo.ThucChayDaTinh
    WHERE TrangThaiHopDong <> 3
      AND NgayThucHien BETWEEN @FromDate AND @ToDate
      AND HopDongID <> 0
      AND Nam >= 2018
      -- AND DotChayBooking = 'HDBAN_INVENTORY' -- Duongnt comment 19-06-2023
      AND HopDongChiTietREF IN (
		SELECT HopDongChiTietID
		FROM dbo.HopDongChiTiet
		WHERE DmLoaiNenTangREF = 9
		   OR HopDongChiTietID IN (
				SELECT HopDongChiTietREF
				FROM DmThongTinHopDongBanInventory
				WHERE DmSanPhamREF <> 733
		   )
	)-- Duongnt add 19-06-2023
    GROUP BY SoHopDong,
             Nam,
             HopDongID,
             HopDongChiTietREF,
             NgayThucHien,
             DmHinhThucQuangCao,
             DmLoaiBannerREF,
             DmSanPhamREF,
             DonViTinh;
END

```
