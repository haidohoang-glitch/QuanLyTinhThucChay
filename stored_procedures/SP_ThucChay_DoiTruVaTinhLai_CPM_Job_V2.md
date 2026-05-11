# Stored Procedure: `ThucChay_DoiTruVaTinhLai_CPM_Job_V2`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2023-08-15 16:18:42.930000
- **Ngày sửa cuối**: 2024-10-10 14:59:52.077000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@dtStart` | `datetime(8)` | No |
| `@dtEnd` | `datetime(8)` | No |
| `@pSoHopDong` | `nvarchar(100)` | No |
| `@pHopDongChiTietID` | `int(4)` | No |
| `@NgayTinh` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
--
/*
EXEC [ThucChay_DoiTruVaTinhLai_CPM_Job_V2]
	@dtStart = '2024-08-01 00:00:00.000' , 
	@dtEnd = '2024-10-09 00:00:00.000' ,
    @pSoHopDong = N'QC4020724' ,
	@pHopDongChiTietID = 735260,
	@NgayTinh = '2024-10-09 00:00:00.000' 
*/

CREATE PROCEDURE [dbo].[ThucChay_DoiTruVaTinhLai_CPM_Job_V2]
	-- Add the parameters for the stored procedure here
	@dtStart DATETIME , 
	@dtEnd DATETIME ,
    @pSoHopDong NVARCHAR(50) ,
	@pHopDongChiTietID INT,
	@NgayTinh DATETIME
AS
BEGIN
	DECLARE @HopDongID INT

	SET @HopDongID = ISNULL((SELECT TOP 1 hd.HopDongID FROM dbo.HopDong hd
	WHERE hd.SoHopDong = @pSoHopDong),0)
	--Tinh Thuc Chay CPM
	--PRINT 'TAO BANNER'
	EXEC [dbo].[ThucChay_HopDongChiTietAndBannerByHopDongID]
	@HopDongID = @HopDongID
	--PRINT 'UPDATE TI LE BANNER'
	EXEC [dbo].[ThucChay_UpdateHopDongChiTietAndBanner_ByHopDong]
	@HopDongID = @HopDongID

	--PRINT 'THUC HIEN DOI TRU VA TINH LAI'
	--THUC HIEN DOI TRU VA TINH LAI
	EXEC [dbo].[sp_TC_DoiTruVaTinhLai_CPM_V2]
					@StartDate = @dtStart
					, @EndDate = @dtEnd
					, @pSoHopDong = @pSoHopDong
					, @pHopDongChiTietID = @pHopDongChiTietID
					, @NgayTinh = @NgayTinh
	
	----Đẩy dl tu [ThucChayDaTinh_DoiTruVaTinhLai_CPM] về ThucChayDaTinh
	EXEC [dbo].[ThucChay_Update_ThucChayDaTinh_To_DoiTruVaTinhLai_CPM]
  	@pHopDongChiTietID = @pHopDongChiTietID,
	@NgayTinh = @NgayTinh

	--Check xem có thanh cong trong viec doi tru va tinh lai 20241004
			INSERT INTO [dbo].[ThongTinThucChayLog]
           ([HopDongChiTietREF]
           ,[HopDongFK]
           ,[DmSanPhamREF]
           ,[ThoiGianLog]
           ,[LoaiLog]
           ,[ContentLog]
           ,[CreatedBy]
           ,[CreatedAt]
           ,[LastModifiedBy]
           ,[LastModifiedAt])

			SELECT  HopDongChiTietREF, HopDongID, DmSanPhamREF, getdate(),0 LoaiLog, 
			N'table [ThucChayDaTinh_DoiTruVaTinhLai_CPM], hd:' + convert(nvarchar(10),HopDongID) + ',sobanghi: ' + Convert(nvarchar(10),count(HopDongChiTietREF)) AS [ContentLog], 
			N'haidh' [CreatedBy],
			GETDATE() [CreatedAt],
			N'haidh' [LastModifiedBy],
            GETDATE() [LastModifiedAt]
			FROM dbo.[ThucChayDaTinh_DoiTruVaTinhLai_CPM]
			group by HopDongID, HopDongChiTietREF, DmSanPhamREF
	
END


```
