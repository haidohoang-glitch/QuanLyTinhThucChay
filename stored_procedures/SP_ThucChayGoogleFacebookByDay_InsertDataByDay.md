# Stored Procedure: `ThucChayGoogleFacebookByDay_InsertDataByDay`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2015-04-08 10:00:21.877000
- **Ngày sửa cuối**: 2015-05-21 12:18:35.470000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@ngayThucHien` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[ThucChayGoogleFacebookByDay_InsertDataByDay]
	-- Add the parameters for the stored procedure here
	@ngayThucHien DateTime
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    TRUNCATE TABLE ThucChayGoogleFacebookByDay
    
	INSERT INTO ThucChayGoogleFacebookByDay
	/*
	SELECT 
		DmSanPhamREF,
		TenSanPham,
		TaiKhoan,
		SoNgayChay,
		Click,
		ThanhTien,
		[Type],
		ThucChayGoogleFacebookID,
		NgayThucHien,
		CreatedAt,
		CreatedBy,
		LastModifiedAt,
		LastModifiedBy,
		0 RecordStatus,
		DeletedStatus
	FROM ThucChayGoogleFacebook A
	WHERE A.NgayThucHien = @ngayThucHien
		AND A.RecordStatus = 1
	*/
	SELECT 
		DmSanPhamREF,
		TenSanPham,
		TaiKhoan,
		sum(SoNgayChay)SoNgayChay,
		sum(Click) CLICK,
		sum(ThanhTien)ThanhTien,
		[Type],
		newid() ThucChayGoogleFacebookID,
		NgayThucHien,
		getdate()CreatedAt,
		'asd'CreatedBy,
		getdate()LastModifiedAt,
		'asd'LastModifiedBy,
		0 RecordStatus,
		0 DeletedStatus
	FROM ThucChayGoogleFacebook A
	WHERE A.NgayThucHien = @ngayThucHien
		AND A.RecordStatus = 1
		AND A.DeletedStatus <> 1
	GROUP BY DmSanPhamREF,
		TenSanPham,
		TaiKhoan,
		[Type],
		NgayThucHien
END

```
