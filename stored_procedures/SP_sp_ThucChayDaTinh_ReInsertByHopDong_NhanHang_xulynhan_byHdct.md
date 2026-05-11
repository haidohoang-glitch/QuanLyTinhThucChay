# Stored Procedure: `sp_ThucChayDaTinh_ReInsertByHopDong_NhanHang_xulynhan_byHdct`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2016-10-20 16:19:13.727000
- **Ngày sửa cuối**: 2016-10-20 16:19:13.727000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |
| `@HopDongChiTietREF` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		doannv
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================



--EXEC [dbo].[sp_ThucChayDaTinh_ReInsertByHopDong_NhanHang_xulynhan] '2016-10-16'
CREATE PROCEDURE [dbo].[sp_ThucChayDaTinh_ReInsertByHopDong_NhanHang_xulynhan_byHdct]
	-- Add the parameters for the stored procedure here
	@NgayThucHien DATETIME, @HopDongChiTietREF INT 
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    -- Insert statements for procedure here
    declare 
	@HopDongID INT,
	@HopDongChiTietID INT	
	DECLARE @out NVARCHAR(2000);

	--TRUNCATE TABLE dbo.ThucChayDaTinh_ThayDoi_xulynhan
	DELETE FROM ThucChayDaTinh_ThayDoi_xulynhan WHERE  HopDongChiTietREF =@HopDongChiTietREF
	--- Update nhan hang bởi thực chạy hd chi tiết
	DECLARE @NhanHangMoi NVARCHAR(500),@HDID INT, @PhanBoID INT 

	DECLARE cursor_hdct CURSOR FOR  
	/*
		SELECT DISTINCT A.* FROM
		(
			SELECT DISTINCT HopDongID, HopDongChiTietID FROM [ABM_Tuyetnta].dbo.NH_THUCTREO_DACHUANHOA_TANGGIAM$
				WHERE 1=1 --AND TinhTrangXulyNhan = 1
				AND DmSanPhamREF NOT IN (141,637,624,375,306,423)
				UNION ALL
				SELECT hdct.HopDongFK, hdct.HopDongChiTietID FROM ABM_Tuyetnta.[dbo].[THUCTREO_CANCHAYLAITINH_v2] D
				INNER JOIN dbo.HopDongChiTiet hdct ON D.HopDongChiTietID = hdct.HopDongChiTietID
				WHERE 1=1
				AND hdct.DmSanPhamREF NOT IN (141,637,624,375,306,423)
		)A
		WHERE A.HopDongID NOT IN (SELECT DISTINCT HopDongREF FROM dbo.DmThongTinHopDongBanInventory)
		*/
		SELECT HopDongFK, HopDongChiTietID FROM dbo.HopDongChiTiet WHERE  HopDongChiTietID =@HopDongChiTietREF
	

	OPEN cursor_hdct   	
	FETCH NEXT FROM cursor_hdct INTO @HDID, @PhanBoID   

	WHILE @@FETCH_STATUS = 0   
	BEGIN   
		EXEC [dbo].[sp_Insert_ThucChayDaTinh_ReInsertByHopDong_NhanHang_xulynhan] @NgayThucHien ,@HDID ,@PhanBoID  
		--EXEC [dbo].[sp_Insert_ThucChayDaTinh_ReInsertByHopDong_NhanHang_xulynhan_khac] @NgayThucHien ,@HDID ,@PhanBoID  
	FETCH NEXT FROM cursor_hdct INTO @HDID,@PhanBoID    
	END   

	CLOSE cursor_hdct   
	DEALLOCATE cursor_hdct
	
END




```
