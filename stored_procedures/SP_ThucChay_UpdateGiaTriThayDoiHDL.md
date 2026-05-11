# Stored Procedure: `ThucChay_UpdateGiaTriThayDoiHDL`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-05-22 12:05:54.557000
- **Ngày sửa cuối**: 2015-09-01 11:41:08.060000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
--EXEC [ThucChay_UpdateGiaTriThayDoiHDL] '2015-05-15'

CREATE PROCEDURE [dbo].[ThucChay_UpdateGiaTriThayDoiHDL] 
-- Add the parameters for the stored procedure here
	@NgayThucHien DATETIME
AS
BEGIN
	DECLARE @HopDongREF INT,
	        @SoHopDong NVARCHAR(50)
	
	DECLARE @DmSanPhamREF INT
	
	
	DECLARE Record_Cursor_HDL CURSOR  
	FOR
	    SELECT DISTINCT a.HopDongID,
	           a.SoHopDong,
	           A.DmSanPhamREF 
	           --a.*, (a.thanhtienthucchay- a.ThanhTienHopDong) lech
	    FROM   (
	               SELECT tcdt.HopDongID,
	                      tcdt.SoHopDong,
	                      tcdt.DmSanPhamREF,
	                      tcdt.TenSanPham,
	                      tcdt.DonViTinh,
	                      SUM(tcdt.SoLuongThucChay+tcdt.SoLuongThayDoi) SoLuongThucChay,
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
	                                     AND hdct.DeletedStatus = 0
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
	                                     AND hdct.DeletedStatus = 0
	                          ),
	                          0
	                      )ThanhTienHopDong
	               FROM   ThucChayDaTinh tcdt
	               WHERE  tcdt.DmSanPhamREF IN (240, 238, 339, 370,598,613)
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
	    WHERE  1=1 and
	    round(a.thanhtienthucchay - a.ThanhTienHopDong,4) > 0
	          -- AND YEAR(tcdt.NgayThucHien) = 2015
	           --AND tcdt.SoHopDong <> 'QC2581213' 
	  --     WHERE  a.SoLuongThucChay >= a.SoluongHopDong AND 
			--abs(a.thanhtienthucchay - a.ThanhTienHopDong) > 1
	  --         AND YEAR(tcdt.NgayThucHien) = 2014 
	  --AND A.SoHopDong = 'QC2950715'
	  
	OPEN Record_Cursor_HDL
	
	-- Perform the first fetch.
	FETCH NEXT FROM Record_Cursor_HDL INTO @HopDongREF, @SoHopDong, @DmSanPhamREF
	
	WHILE @@FETCH_STATUS = 0
	BEGIN
	    --UPDATE GIA TRI THAY DOI CUA THUCCHAYDATINH = 0
	    PRINT @SoHopDong
	    PRINT @DmSanPhamREF
	    EXEC [ThucChay_UpdateGiaTriThayDoiThucChayDaTinhCPMByNgayThucHien] @NgayThucHien,
	         @SoHopDong,
	         0,
	         @DmSanPhamREF
	    
	    FETCH NEXT FROM Record_Cursor_HDL INTO @HopDongREF, @SoHopDong, @DmSanPhamREF
	END
	CLOSE Record_Cursor_HDL
	DEALLOCATE Record_Cursor_HDL
	SELECT 1
END

--EXEC [ThucChay_UpdateGiaTriThayDoiHDL] '2014-07-22'

```
