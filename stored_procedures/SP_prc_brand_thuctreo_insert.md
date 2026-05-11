# Stored Procedure: `prc_brand_thuctreo_insert`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2019-05-27 10:47:38.833000
- **Ngày sửa cuối**: 2019-05-27 10:47:38.833000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		Doannv
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[prc_brand_thuctreo_insert] 
	-- Add the parameters for the stored procedure here
	@NgayThucHien datetime = '2016-04-11'
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    --Nhan Hang có tên chưa có id bên thực treo
	select TenNhanHang into #NhanHang from 
	(
	select TenNhanHang from ThucTreo where isnull(Dm_NhanHang_Id,0) = 0 AND convert(date,[Last_Modified_At]) = @NgayThucHien
	union 
	select Brand_Name from ThucTreo_ChiPhi where isnull(Brand_Id,0) = 0 AND convert(date,LastModifiedAt) = @NgayThucHien
	union
	select TenNhanHang from ThucTreo_PR where isnull(NhanHang_Id,0) = 0 AND convert(date,[Last_Modified_At]) = @NgayThucHien
	) A
	-- nhan đã có id bên BRAND 
	select A.DmNhanHangID, A.TenNhanHang into #NhanCoID from BRAND.dbo.DmNhanHang A inner join #NhanHang B on A.TenNhanHang = B.TenNhanHang AND A.DeletedStatus = 0
	-- update 
	update ThucTreo set Dm_NhanHang_Id = B.DmNhanHangID, Last_Modified_At = GETDATE()
	from ThucTreo A inner join #NhanCoID B on A.TenNhanHang = B.TenNhanHang AND convert(date,A.[Last_Modified_At]) = @NgayThucHien
	update ThucTreo_PR set NhanHang_Id = B.DmNhanHangID,Last_Modified_At = GETDATE()
	from ThucTreo_PR A inner join #NhanCoID B on A.TenNhanHang = B.TenNhanHang AND convert(date,A.[Last_Modified_At]) = @NgayThucHien
	update ThucTreo_ChiPhi set Brand_Id = B.DmNhanHangID,LastModifiedAt = GETDATE()
	from ThucTreo_ChiPhi A inner join #NhanCoID B on A.Brand_Name = B.TenNhanHang AND convert(date,A.LastModifiedAt) = @NgayThucHien
	-- Nhan Hang chuan hoa sang nhan khac 
	select ROW_NUMBER() over(order by LastModifiedAt) as stt, DmNhanHangID,DmNhanHangThayDoiID into #NhanHangChuanHoa from BRAND.dbo.DmNhanHang where CONVERT(date,LastModifiedAt) = @NgayThucHien and ISNULL(DmNhanHangThayDoiID,0) <> 0

	-----
	declare @NhanHangID int, @NhanChuanHoaID int
	DECLARE db_cursor_nhan CURSOR FOR 
	select DmNhanHangID,DmNhanHangThayDoiID from  #NhanHangChuanHoa order by stt

	OPEN db_cursor_nhan  
	FETCH NEXT FROM db_cursor_nhan INTO @NhanHangID  ,@NhanChuanHoaID

	WHILE @@FETCH_STATUS = 0  
	BEGIN 
	 
		 update ThucTreo set Dm_NhanHang_Id = @NhanChuanHoaID,Last_Modified_At = getdate() where Dm_NhanHang_Id = @NhanHangID
		 update ThucTreo_ChiPhi set Brand_Id = @NhanChuanHoaID, LastModifiedAt = getdate() where Brand_Id = @NhanHangID
		 update ThucTreo_PR set NhanHang_Id = @NhanChuanHoaID,Last_Modified_At = getdate() where NhanHang_Id = @NhanHangID

		 FETCH NEXT FROM db_cursor_nhan INTO @NhanHangID  ,@NhanChuanHoaID 
	END 

	CLOSE db_cursor_nhan  
	DEALLOCATE db_cursor_nhan 
	-----

	drop table #NhanHang
	drop table #NhanCoID
	drop table #NhanHangChuanHoa

END

```
