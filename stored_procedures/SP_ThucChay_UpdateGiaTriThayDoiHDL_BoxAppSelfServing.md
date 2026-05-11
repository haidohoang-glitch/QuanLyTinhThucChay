# Stored Procedure: `ThucChay_UpdateGiaTriThayDoiHDL_BoxAppSelfServing`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-06-04 16:39:30.953000
- **Ngày sửa cuối**: 2014-11-19 12:16:58.210000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		PHUONGTM
-- Create date: 2014-06-04
-- Description:	Update Gia Tri Thay Doi Hop Dong Lech - BoxAppSelfServing
-- =============================================

-- EXEC [ThucChay_UpdateGiaTriThayDoiHDL_BoxAppSelfServing] '2014-06-09'
CREATE PROCEDURE [dbo].[ThucChay_UpdateGiaTriThayDoiHDL_BoxAppSelfServing] 
-- Add the parameters for the stored procedure here
	@NgayThucHien DATETIME
AS
BEGIN
	DECLARE @HopDongREF INT,
	        @SoHopDong NVARCHAR(50)
	DECLARE @DmSanPhamREF INT	
	DECLARE Record_Cursor_HDL CURSOR  
	FOR
	SELECT DISTINCT 
			a.HopDongID,
			a.SoHopDong,
			A.DmSanPhamREF 
            --a.*, 
            --(a.SoLuongThucChay - a.SoluongHopDong) Lech,
            --(a.thanhtienthucchay- a.ThanhTienHopDong) LechTien
     FROM   (
                SELECT tcdt.HopDongID,
                       tcdt.SoHopDong,
                       tcdt.DmSanPhamREF,
                       tcdt.TenSanPham,
                       tcdt.DonViTinh,
                       SUM(tcdt.SoLuongThucChay) SoLuongThucChay,
                       ISNULL(
                           (
                               SELECT (
                                          CASE 
                                               WHEN tcdt.DonViTinh = 'VIEW' THEN 
                                                    ROUND(ISNULL(SUM(hdct.SoLuong), 0) * 1000, 0)
                                               ELSE ISNULL(SUM(hdct.SoLuong), 0)
                                          END
                                      ) AS SoluongHopDong
                               FROM   HopDong hd
                                      INNER JOIN HopDongChiTiet hdct
                                           ON  hd.HopDongID = hdct.HopDongFK
                               WHERE  hd.HopDongID = tcdt.HopDongID
                                      AND hdct.DmSanPhamREF = tcdt.DmSanPhamREF
                                      AND hdct.IsKhuyenMai = 0
                           ),
                           0
                       ) SoluongHopDong,
                       SUM(tcdt.ThanhTienSauTrietKhauThucChay + tcdt.GiaTriThayDoi) 
                       thanhtienthucchay,
                       ISNULL(
                           (
                               SELECT SUM(hdct.ThanhTien) soluong
                               FROM   HopDong hd
                                      INNER JOIN HopDongChiTiet hdct
                                           ON  hd.HopDongID = hdct.HopDongFK
                               WHERE  hd.HopDongID = tcdt.HopDongID
                                      AND hdct.DmSanPhamREF = tcdt.DmSanPhamREF
                                      AND hdct.IsKhuyenMai = 0
                           ),
                           0
                       )ThanhTienHopDong
                FROM   ThucChayDaTinh tcdt
                WHERE  tcdt.DmSanPhamREF IN (375)
                AND (tcdt.DonViTinh = 'VIEW' OR tcdt.DonViTinh = 'CLICK')
                GROUP BY
                       tcdt.SoHopDong,
                       tcdt.HopDongID,
                       tcdt.DmSanPhamREF,
                       tcdt.TenSanPham,
                       tcdt.DonViTinh,
                       tcdt.HopDongID,
                       tcdt.DonViTinh
            )A
            INNER JOIN (
                     SELECT tcdt.SoHopDong,
                            tcdt.HopDongID,
                            tcdt.DmSanPhamREF,
                            tcdt.DonViTinh,
                            MAX(tcdt.NgayThucHien) NgayThucHien
                     FROM   ThucChayDaTinh tcdt
                     GROUP BY
                            tcdt.SoHopDong,
                            tcdt.HopDongID,
                            tcdt.DmSanPhamREF,
                            tcdt.DonViTinh
                 ) tcdt
                 ON  tcdt.HopDongID = a.HopDongID
                 AND tcdt.DmSanPhamREF = a.DmSanPhamREF
                 AND tcdt.DonViTinh = a.DonViTinh
     WHERE  YEAR(tcdt.NgayThucHien) = 2014
            and tcdt.HopDongID <> 0 
            and (tcdt.SoHopDong <> '' or tcdt.SoHopDong <> '-' or tcdt.SoHopDong <> '0') 
            AND round(a.thanhtienthucchay - a.ThanhTienHopDong,4) > 0
	OPEN Record_Cursor_HDL
	-- Perform the first fetch.
	FETCH NEXT FROM Record_Cursor_HDL INTO @HopDongREF, @SoHopDong, @DmSanPhamREF
	WHILE @@FETCH_STATUS = 0
	BEGIN
	    --UPDATE GIA TRI THAY DOI CUA THUCCHAYDATINH = 0
	    PRINT @SoHopDong
	    PRINT @DmSanPhamREF
	    EXEC [ThucChay_UpdateGiaTriTDBoxAppSelfServingVGTHD] @NgayThucHien,
	         @HopDongREF,
	         @DmSanPhamREF,
	         ''
	    FETCH NEXT FROM Record_Cursor_HDL INTO @HopDongREF, @SoHopDong, @DmSanPhamREF
	END
	CLOSE Record_Cursor_HDL
	DEALLOCATE Record_Cursor_HDL
	SELECT 1
END

```
