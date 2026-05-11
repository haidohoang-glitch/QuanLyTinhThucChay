# Stored Procedure: `job_ThucChayDaTinh_ReInsertByHopDong_SanPham_NgayThucHien`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2018-08-24 17:35:59.630000
- **Ngày sửa cuối**: 2018-08-24 17:42:52.727000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |
| `@DmSanPhamREF` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[job_ThucChayDaTinh_ReInsertByHopDong_SanPham_NgayThucHien]
	@NgayThucHien DATETIME,
	@DmSanPhamREF INT

AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

	--1. SP Thực hiện việc check và tính giá trị thay đổi khi hợp đồng thay đổi thay đổi nội dung
	EXEC [dbo].[sp_ThucChayDaTinh_ReInsertByHopDong_NgayThucHien_SanPham]
		@NgayThucHien = @NgayThucHien,
		@DmSanPhamREF = @DmSanPhamREF 
	--2. SP thực hiện việc check và tính giá trị thay đổi khi thực treo nhãn hàng thay đổi
	EXEC [dbo].[sp_ThucChayDaTinh_ReInsertByHopDong_NhanHang_NgayThucHien_SanPham]
		@NgayThucHien = @NgayThucHien,
		@DmSanPhamREF = @DmSanPhamREF


END

```
