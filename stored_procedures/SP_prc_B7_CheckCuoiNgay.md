# Stored Procedure: `prc_B7_CheckCuoiNgay`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2022-04-29 15:01:54.307000
- **Ngày sửa cuối**: 2022-04-29 17:44:39.567000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@ngayThucHien1` | `datetime(8)` | No |
| `@ngayThucHien2` | `datetime(8)` | No |

## Definition (Source Code)

```sql

CREATE PROC prc_B7_CheckCuoiNgay
	@ngayThucHien1 DATETIME = NULL,
	@ngayThucHien2 DATETIME = NULL
AS
BEGIN
    SET NOCOUNT ON;

	DECLARE @ngayTest DATE = '1975-01-01';


	IF(@ngayThucHien1 = @ngayTest AND @ngayThucHien2 = @ngayTest)
	BEGIN
		RETURN;
	END

    SELECT SoHopDong,
           HopDongID,
           HopDongChiTietREF,
           DmSanPhamREF,
           DmLoaiBannerREF,
           DmHinhThucQuangCao,
           NhanHang,
           SUM(ThanhTienSauTrietKhauThucChay) tt,
           SUM(GiaTriThayDoi) td,
           NgayThucHien
    FROM ThucChayDaTinh
    WHERE NgayThucHien >= @ngayThucHien1
          AND HopDongID <> 0 AND Nam <= (
		   SELECT MAX(YEAR(NgayThucHien))  -3 FROM ThucChayDaTinh
		  ) 
    GROUP BY SoHopDong,
             HopDongID,
             HopDongChiTietREF,
             DmSanPhamREF,
             NgayThucHien,
             DmLoaiBannerREF,
             DmHinhThucQuangCao,
             NhanHang
          

    --b2. tao bang contract, lay du lieu cac hd tu nam 2015

    EXEC CheckThucChayVuotHopDong_TableHopDong;

    --B3. tao bang thucchaydatinh, lay du lieu cac hd tu nam 2015

    EXEC CheckThucChayVuotHopDong_TableTCDT @ngayThucHien1, @ngayThucHien2; -- truyền ngày thực hiện đã tính thực chạy

    --b4. Check vuot
    EXEC dbo.CheckThucChayVuotHopDong_v2 @NgayThucHien = @ngayThucHien2, -- datetime								
                                         @LoaiCheck = 1;
    EXEC dbo.CheckThucChayVuotHopDong_v2 @NgayThucHien = @ngayThucHien2, -- datetime								
                                         @LoaiCheck = 2;

    --B6. Kiểm tra hợp đồng có tổng thực chạy ghi nhận âm
    --Không cho phép ghi nhận tổng giá trị thực chạy theo hợp đồng âm (trừ 1 số trường hợp của mua ngoài do ghi nhận lỗ)
    SELECT SoHopDong,
           HopDongID,
           HopDongChiTietID,
           DmSanPhamREF,
           SUM(ThanhTienThucChay)
    FROM KS_ThucChay_TCDT
    WHERE Nam >= (
		   SELECT MAX(YEAR(NgayThucHien))  -3 FROM ThucChayDaTinh
		  ) 
          AND HopDongChiTietID NOT IN ( 595304 ) --loại phân bổ do phân bổ mua ngoài accepted ghi nhận lỗ
    GROUP BY SoHopDong,
             HopDongID,
             HopDongChiTietID,
             DmSanPhamREF
    HAVING ROUND(SUM(ThanhTienThucChay), 0) < 0;

END;


```
