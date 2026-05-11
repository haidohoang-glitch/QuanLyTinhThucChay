# Stored Procedure: `ThucChayKiemTra_CPM_Insert_Manual_v2`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-01-11 15:09:30.187000
- **Ngày sửa cuối**: 2017-06-09 15:52:07.430000

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

--EXEC ThucChayKiemTra_CPM_Insert_Manual '2015-07-05' -- chạy lệnh này để kiểm tra các hợp dồng cần check

CREATE PROCEDURE [dbo].[ThucChayKiemTra_CPM_Insert_Manual_v2]
-- Add the parameters for the stored procedure here
	@NgayThucHien DATETIME
AS
BEGIN
	--Insert ThucChayCPM By @NgayThucHien
	EXEC [dbo].[ThucChayCPM_Insert_Manual] @NgayThucHien
	
	--Delete Data
	DELETE 
	FROM   dbo.ThucChayKiemTra_CPM
	WHERE  NgayThucHien = @NgayThucHien
	--Insert TongViewKiemTra, TongClickKiemTra
	INSERT INTO dbo.ThucChayKiemTra_CPM
	SELECT SoHopDong,
	       NgayThucHien,
	       dbo.GetProductIDByTypeProduct(typeproduct) AS DmSanPhamREF,
	       dbo.GetProductNameByTypeProduct(typeproduct) AS TenSanPham,
	       0,
	       SUM(TongView) AS TongViewKiemTra,
	       0,
	       SUM(TongClick) AS TongClickKiemTra,
	       0,
	       0,
	       '',
	       ''
	FROM   dbo.ThucChayCPM
	WHERE  dbo.GetProductIDByTypeProduct(typeproduct) IN (231, 238, 339, 342, 337, 240, 370, 598,613,732,735)
	       AND NgayThucHien = @NgayThucHien
		   AND CONVERT(NVARCHAR(50),bannerid) NOT IN (SELECT DmBannerREF FROM dbo.ThucChayHopDongChiTiet WHERE DmHinhThucQuangCaoREF = 42 AND DeletedStatus = 0)
	GROUP BY
	       SoHopDong,
	       NgayThucHien,
	       typeproduct
	
	--Insert TongViewDaTinh, TongClickDaTinh
	DECLARE @SoHopDong        NVARCHAR(50),
	        @DmSanPhamREF     INT,
	        @TongViewDaTinh   FLOAT,
	        @TongClickDaTinh  FLOAT
	
	
	DECLARE Record_Cursor CURSOR  
	FOR
	    SELECT A.SoHopDong,
	           A.NgayThucHien,
	           A.DmSanPhamREF
	    FROM   dbo.ThucChayKiemTra_CPM A
	    WHERE  CONVERT(VARCHAR(50), A.NgayThucHien, 103) = CONVERT(VARCHAR(50), @NgayThucHien, 103)
	
	OPEN Record_Cursor
	
	-- Perform the first fetch.
	FETCH NEXT FROM Record_Cursor INTO @SoHopDong,@NgayThucHien,@DmSanPhamREF
	
	WHILE @@FETCH_STATUS = 0
	BEGIN
	    SET @TongViewDaTinh = (
	            SELECT SUM(TongViewThucChay)
	            FROM   dbo.ThucChayDaTinh
	            WHERE  SoHopDong = @SoHopDong
	                   AND CONVERT(VARCHAR(50), NgayThucHien, 103) = CONVERT(VARCHAR(50), @NgayThucHien, 103)
	                   AND DmSanPhamREF = @DmSanPhamREF
	        )
	    
	    SET @TongViewDaTinh = ISNULL(@TongViewDaTinh, 0)
	    SET @TongClickDaTinh = (
	            SELECT SUM(TongClickThucChay)
	            FROM   dbo.ThucChayDaTinh
	            WHERE  SoHopDong = @SoHopDong
	                   AND CONVERT(VARCHAR(50), NgayThucHien, 103) = CONVERT(VARCHAR(50), @NgayThucHien, 103)
	                   AND DmSanPhamREF = @DmSanPhamREF
	        )
	    
	    SET @TongClickDaTinh = ISNULL(@TongClickDaTinh, 0)
	    
	    
	    UPDATE dbo.ThucChayKiemTra_CPM
	    SET    TongViewDaTinh = @TongViewDaTinh,
	           TongClickDaTinh = @TongClickDaTinh,
	           NoiDungLoi = dbo.ThucChay_XacDinhLoi(
	               @SoHopDong,
	               @DmSanPhamREF,
	               @TongViewDaTinh,
	               TongViewKiemTra
	           ),
	           TrangThaiLoi = dbo.ThucChay_XacDinhMaLoi(
	               @SoHopDong,
	               @DmSanPhamREF,
	               @TongViewDaTinh,
	               TongViewKiemTra
	           )
	    WHERE  SoHopDong = @SoHopDong
	           AND CONVERT(VARCHAR(50), NgayThucHien, 103) = CONVERT(VARCHAR(50), @NgayThucHien, 103)
	           AND DmSanPhamREF = @DmSanPhamREF
	    -- Perform the first fetch.
	    FETCH NEXT FROM Record_Cursor INTO @SoHopDong,@NgayThucHien,@DmSanPhamREF
	END
	
	CLOSE Record_Cursor
	DEALLOCATE Record_Cursor
	
	EXEC ThucChay_QuanLyLoiCPM -1,
	     @NgayThucHien,
	     @NgayThucHien,
	     1
END

```
