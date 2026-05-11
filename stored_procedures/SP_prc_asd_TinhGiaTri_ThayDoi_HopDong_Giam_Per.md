# Stored Procedure: `prc_asd_TinhGiaTri_ThayDoi_HopDong_Giam_Per`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-09-11 15:02:52.473000
- **Ngày sửa cuối**: 2023-12-13 10:24:15.610000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |
| `@PhanBo_ID` | `int(4)` | No |
| `@DmSanPham_ID` | `int(4)` | No |
| `@TenSanPham` | `nvarchar(400)` | No |
| `@GiaTriGiam` | `money(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		Doannv
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[prc_asd_TinhGiaTri_ThayDoi_HopDong_Giam_Per]
	-- Add the parameters for the stored procedure here
	@NgayThucHien datetime,
	@PhanBo_ID int,
	@DmSanPham_ID int,
	@TenSanPham nvarchar(200),
	@GiaTriGiam money
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    -- Insert statements for procedure here
	print 2
	declare 
	@sohopdong nvarchar(50),
	@HopDongChiTietREF int,
	@DmWebsiteREF int,
	@TenWebsite nvarchar(500),
	@DonViTinh nvarchar(10),
    @NhanHang nvarchar(200),
	@ThanhTien money,
	@Record_GiaTriGiam money,@TongGiatri money

	set @TongGiatri = isnull((select SUM(isnull(GiaTriThayDoi,0)+isnull(ThanhTienSauTrietKhauThucChay,0)) 
	from ThucChayDaTinhAdmarket where HopDongChiTietREF = @PhanBo_ID and DmSanPhamREF = @DmSanPham_ID),0)

	

	DECLARE db_cursor_chitiet CURSOR FOR  
	select sohopdong,HopDongChiTietREF,DmWebsiteREF,TenWebsite,DonViTinh,NhanHang, SUM(isnull(GiaTriThayDoi,0)+isnull(ThanhTienSauTrietKhauThucChay,0)) 
	from ThucChayDaTinhAdmarket
	where 
	HopDongChiTietREF = @PhanBo_ID and DmSanPhamREF = @DmSanPham_ID
	group by 
	sohopdong,HopDongChiTietREF,DmWebsiteREF,TenWebsite,DonViTinh,NhanHang

	OPEN db_cursor_chitiet   
	FETCH NEXT FROM db_cursor_chitiet INTO @sohopdong  ,@HopDongChiTietREF,@DmWebsiteREF,@TenWebsite,@DonViTinh,@NhanHang,@ThanhTien

	WHILE @@FETCH_STATUS = 0   
	BEGIN   
	
	       IF @TongGiatri <> 0  set @Record_GiaTriGiam = -@ThanhTien * @GiaTriGiam /@TongGiatri
		   ELSE set @Record_GiaTriGiam = 0
		   print @GiaTriGiam
		   print @TongGiatri
		   print @ThanhTien
		   print @Record_GiaTriGiam
		   exec [dbo].[prc_asd_ThucChayDaTinhAdmarket_InsertByPhanBoID_ThayDoiHopDong]
					@ngaythuchien,
					@SoHopDong,
					@PhanBo_ID,
					@DmSanPham_ID,
					@TenSanPham,
					@DmWebsiteREF,
					@TenWebsite,
					0,
					0,
					0,
					@Record_GiaTriGiam,
					0,
					0,
					0,
					0,
					1,
					@DonViTinh,
					N'Thuc_Chay_Admarket Đổ online giảm gt hợp đồng ',
					0,
					'',
					@NhanHang

		   FETCH NEXT FROM db_cursor_chitiet INTO @sohopdong  ,@HopDongChiTietREF,@DmWebsiteREF,@TenWebsite,@DonViTinh,@NhanHang,@ThanhTien 
	END   

	CLOSE db_cursor_chitiet   
	DEALLOCATE db_cursor_chitiet
	
END


```
