# Function: `BaoCaoThongTinTongHop_FilterChiTiet`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2013-12-04 09:12:25.150000
- **Ngày sửa cuối**: 2014-10-14 10:39:37.983000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `nvarchar(8000)` | Yes |
| `@DmNghanhHangREFList` | `nvarchar(8000)` | No |
| `@DmNhanHangREFList` | `nvarchar(8000)` | No |
| `@DmLoaiSanPhamREFList` | `nvarchar(8000)` | No |
| `@DmSanPhamREFList` | `nvarchar(8000)` | No |
| `@DmNhomWebsiteREFList` | `nvarchar(8000)` | No |
| `@DmWebsiteREFList` | `nvarchar(8000)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date, ,>
-- Description:	<Description, ,>
-- =============================================
CREATE FUNCTION [dbo].[BaoCaoThongTinTongHop_FilterChiTiet]
(	
	--Nhãn hàng, nghành hàng
	 @DmNghanhHangREFList nvarchar(4000)
	,@DmNhanHangREFList nvarchar(4000)
	--Thông tin sản phẩm
	,@DmLoaiSanPhamREFList nvarchar(4000)
	,@DmSanPhamREFList nvarchar(4000)
	--Thông tin Website
	,@DmNhomWebsiteREFList nvarchar(4000)
	,@DmWebsiteREFList nvarchar(4000)	
)
RETURNS nvarchar(4000)
AS
BEGIN

	Declare @FilterChiTiet nvarchar(4000), @KhachHangFilter nvarchar(4000)
	set @KhachHangFilter = '1=1'
	
	--Nhãn hàng, nghành hàng
	if(@DmNghanhHangREFList is not null and @DmNghanhHangREFList <> '')
		set @KhachHangFilter = @KhachHangFilter + ' and ' + 'DmNghanhHangREF in (' + @DmNghanhHangREFList + ')'	

	if(@DmNhanHangREFList is not null and @DmNhanHangREFList <> '')
		set @KhachHangFilter = @KhachHangFilter + ' and ' + 'DmNhanHangREF in (' + @DmNhanHangREFList + ')'		
	
	--Thông tin sản phẩm
	Declare @SanPhamFilter nvarchar(4000)
	set @SanPhamFilter = '1=1'
	
	if(@DmLoaiSanPhamREFList is not null and @DmLoaiSanPhamREFList <> '')
		set @SanPhamFilter = @SanPhamFilter + ' and ' + 'DmLoaiSanPhamREF in (' + @DmLoaiSanPhamREFList + ')'	
	
	if(@DmSanPhamREFList is not null and @DmSanPhamREFList <> '')
		set @SanPhamFilter = @SanPhamFilter + ' and ' + 'DmSanPhamREF in (' + @DmSanPhamREFList + ')'		
		
	--Thông tin Website
	Declare @WebsiteFilter nvarchar(4000)
	set @WebsiteFilter = '1=1'
	
	if(@DmNhomWebsiteREFList is not null and @DmNhomWebsiteREFList <> '')
		set @WebsiteFilter = @WebsiteFilter + ' and ' + 'DmNhomWebsiteREF in (' + @DmNhomWebsiteREFList + ')'	
	
	if(@DmWebsiteREFList is not null and @DmWebsiteREFList <> '')
		set @WebsiteFilter = @WebsiteFilter + ' and ' + 'DmWebsiteREF in (' + @DmWebsiteREFList + ')'	

	
	set @FilterChiTiet = @KhachHangFilter + ' and ' + @SanPhamFilter + ' and ' + @WebsiteFilter
	
	-- Return the result of the function
	RETURN @FilterChiTiet

END

```
