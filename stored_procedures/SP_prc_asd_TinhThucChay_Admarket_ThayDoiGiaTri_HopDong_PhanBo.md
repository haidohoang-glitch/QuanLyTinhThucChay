# Stored Procedure: `prc_asd_TinhThucChay_Admarket_ThayDoiGiaTri_HopDong_PhanBo`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2024-02-06 11:03:49.530000
- **Ngày sửa cuối**: 2024-02-28 11:35:35.100000

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
-- exec [dbo].[prc_asd_TinhThucChay_Admarket_ThayDoiGiaTri_HopDong] '2017-09-05'
-- =============================================
CREATE PROCEDURE [dbo].[prc_asd_TinhThucChay_Admarket_ThayDoiGiaTri_HopDong_PhanBo]
	-- Add the parameters for the stored procedure here
	@NgayThucHien datetime
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    -- Insert statements for procedure here
	declare @stt int , @HopDongFK int, @HopDongChiTietREF int, @DmSanPhamREF int, @TenSanPham nvarchar(200),@ThanhTien float, @ThanhTien_old float;
	
	DECLARE db_cursor CURSOR FOR  
	select A.*,B.ThanhTien from 
	(
		select 
		Row_number() over(partition by HopDongChiTietREF order by HopDongChiTietLogID desc  ) stt,
		HopDongFK,
		HopDongChiTietREF,
		DmSanPhamREF,
		(case when DmSanPhamREF = 628 then 'Viewplus' 
		when DmSanPhamREF = 144 then 'CPC Admarket' 
		when  DmSanPhamREF = 585 then 'AdX'  else TenSanPham 
		end) TenSanPham,
		ThanhTien
		from HopDongChiTietLog where DmSanPhamREF in (628,585,144) and convert(date,ThoiGianLog) = @NgayThucHien
	) A
	inner join
	(
		select 
		Row_number() over(partition by HopDongChiTietREF order by HopDongChiTietLogID desc  ) stt,
		HopDongFK,
		HopDongChiTietREF,
		DmSanPhamREF,
		case when DmSanPhamREF = 628 then 'Viewplus' 
		when DmSanPhamREF = 144 then 'CPC Admarket' 
		when  DmSanPhamREF = 585 then 'AdX'  else TenSanPham end TenSanPham,
		ThanhTien
		from HopDongChiTietLog where DmSanPhamREF in (628,585,144) and convert(date,ThoiGianLog) < @NgayThucHien
	) B on A.HopDongChiTietREF = B.HopDongChiTietREF
	and A.stt = 1 and B.stt = 1 and A.ThanhTien <> B.ThanhTien
	OPEN db_cursor   
	FETCH NEXT FROM db_cursor INTO @stt  , @HopDongFK , @HopDongChiTietREF , @DmSanPhamREF , @TenSanPham ,@ThanhTien , @ThanhTien_old  

	WHILE @@FETCH_STATUS = 0   
	BEGIN   
		   
		   exec dbo.[prc_asd_TinhGiaTri_ThayDoi_HopDong_Per_PhanBo] @NgayThucHien,@HopDongFK,@HopDongChiTietREF,@DmSanPhamREF , @TenSanPham,@ThanhTien , @ThanhTien_old;    
		   FETCH NEXT FROM db_cursor INTO @stt  , @HopDongFK , @HopDongChiTietREF , @DmSanPhamREF , @TenSanPham ,@ThanhTien , @ThanhTien_old    
	END   

	CLOSE db_cursor   
	DEALLOCATE db_cursor
	
END

```
