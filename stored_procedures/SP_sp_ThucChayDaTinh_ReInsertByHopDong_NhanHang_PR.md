# Stored Procedure: `sp_ThucChayDaTinh_ReInsertByHopDong_NhanHang_PR`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2019-05-31 16:29:28.550000
- **Ngày sửa cuối**: 2019-06-20 15:17:31.120000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |
| `@ThucChayHopDongChiTietID` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		doannv
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
/*
EXEC [dbo].[sp_ThucChayDaTinh_ReInsertByHopDong_NhanHang_PR] '2019-05-30'
*/

CREATE PROCEDURE [dbo].[sp_ThucChayDaTinh_ReInsertByHopDong_NhanHang_PR]
	-- Add the parameters for the stored procedure here
	@NgayThucHien DATETIME,
	@ThucChayHopDongChiTietID INT
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    DECLARE @HopDongREF INT, @DmSanPhamREF INT, @ThucChayHopDongChiTietPRID INT

	DECLARE cursor_hdct_pr_nhan CURSOR FOR  
		SELECT HopDongREF, DmSanPhamREF, ThucChayHopDongChiTietPRID FROM dbo.ThucChayHopDongChiTietPR
		WHERE DeletedStatus = 0
		--AND CONVERT(DATE,LastModifiedAt) = @NgayThucHien
		AND RecordStatus = 1 --Check nhung truong hop da duoc tinh thuc chay roi
		AND (ISNULL(NhanHang,'0') <> '0' OR ISNULL(NhanHang,'') <> '')
		AND CONVERT(DATE,CreatedAt) < CONVERT(DATE,LastModifiedAt)
		AND ThucChayHopDongChiTietPRID  = @ThucChayHopDongChiTietID

		OPEN cursor_hdct_pr_nhan   	
	FETCH NEXT FROM cursor_hdct_pr_nhan INTO @HopDongREF, @DmSanPhamREF, @ThucChayHopDongChiTietPRID

	WHILE @@FETCH_STATUS = 0   
	BEGIN   
		PRINT @ThucChayHopDongChiTietPRID
		EXEC [dbo].[sp_Insert_ThucChayDaTinh_ReInsertByHopDong_NhanHang_PR]
		@NgayThucHien = @NgayThucHien,
		@HopDongID = @HopDongREF,
		@DmSanPhamREF = @DmSanPhamREF,
		@ThucChayHopDongChiTietPRID = @ThucChayHopDongChiTietPRID
		
	FETCH NEXT FROM cursor_hdct_pr_nhan INTO @HopDongREF, @DmSanPhamREF, @ThucChayHopDongChiTietPRID  
	END   

	CLOSE cursor_hdct_pr_nhan   
	DEALLOCATE cursor_hdct_pr_nhan
	
END



```
