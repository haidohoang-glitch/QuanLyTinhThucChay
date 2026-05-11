# Stored Procedure: `ThucChay_TinhCPD_By_NgayThucHien`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-07-13 15:17:08.710000
- **Ngày sửa cuối**: 2017-07-13 15:17:49.217000

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
--
/*
EXEC [dbo].[ThucChay_TinhCPD_By_NgayThucHien] '2017-07-15'
*/

CREATE PROCEDURE [dbo].[ThucChay_TinhCPD_By_NgayThucHien]
	@NgayThucHien DATETIME
AS
BEGIN
	--Update gia tri thay doi CPD
	SET @NgayThucHien = CONVERT(date,@NgayThucHien)

 	--Tinh Thuc Chay CPD
	EXEC [ThucChay_InsertThucChayDaTinh_CPD_DotChay] @NgayThucHien,@NgayThucHien
	--Tinh Thuc Chay CPD Khong Dot Chay
	PRINT 'Insert CPD Khong Dot Chay'
	EXEC [ThucChay_InsertThucChayDaTinh_CPD_KhongDotChay] @NgayThucHien,@NgayThucHien
	
	
	EXEC [ThucChay_UpdateGiaTriThayDoiThucChayDaTinh_CPD] @NgayThucHien
	EXEC [ThucChay_UpdateGiaTriThayDoiThucChayDaTinh_CPDDonGiaTheoDVT] @NgayThucHien
	EXEC [ThucChay_UpdateGiaTriThayDoiThucChayDaTinh_CPDDotChayTD] @NgayThucHien

END

```
