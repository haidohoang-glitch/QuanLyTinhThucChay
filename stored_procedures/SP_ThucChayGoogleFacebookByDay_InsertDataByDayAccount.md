# Stored Procedure: `ThucChayGoogleFacebookByDay_InsertDataByDayAccount`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2015-04-08 10:00:21.720000
- **Ngày sửa cuối**: 2015-04-08 10:00:21.720000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@ngayThucHien` | `datetime(8)` | No |
| `@account` | `nvarchar(100)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[ThucChayGoogleFacebookByDay_InsertDataByDayAccount]
	-- Add the parameters for the stored procedure here
	@ngayThucHien	DATETIME,
	@account		NVARCHAR(50)
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    TRUNCATE TABLE ThucChayGoogleFacebookByDay
    
	INSERT INTO ThucChayGoogleFacebookByDay
	SELECT 
		DmSanPhamREF,
		TenSanPham,
		TaiKhoan,
		SUM(SoNgayChay) SoNgayChay,
		SUM(Click) Click,
		SUM(ThanhTien) ThanhTien,
		[Type],
		NEWID() ThucChayGoogleFacebookID,
		@ngayThucHien NgayThucHien,
		GETDATE() CreatedAt,
		'asd' CreatedBy,
		GETDATE() LastModifiedAt,
		'asd' LastModifiedBy,
		0 RecordStatus,
		DeletedStatus
	FROM ThucChayGoogleFacebook A
	WHERE A.NgayThucHien = @ngayThucHien
		AND A.RecordStatus = 1
		AND A.TaiKhoan = @account
	GROUP BY
		DmSanPhamREF,
		TenSanPham,
		TaiKhoan,
		[Type],
		DeletedStatus
END

```
