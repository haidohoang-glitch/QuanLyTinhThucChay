# Stored Procedure: `ThucChayDaTinhOther_Insert`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-12-16 13:39:42.973000
- **Ngày sửa cuối**: 2014-12-16 13:39:42.973000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@sanPhamId` | `int(4)` | No |
| `@tenSanPham` | `nvarchar(100)` | No |
| `@soLuongThucChay` | `int(4)` | No |
| `@tienThucChay` | `float(8)` | No |
| `@ghiChu` | `nvarchar(2000)` | No |
| `@userActive` | `nvarchar(100)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		NhatMQ
-- Create date: 2014-12-13
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[ThucChayDaTinhOther_Insert]
	-- Add the parameters for the stored procedure here
	@sanPhamId		INT,
	@tenSanPham		NVARCHAR(50),
	@soLuongThucChay	INT,
	@tienThucChay		FLOAT,
	@ghiChu				NVARCHAR(1000),
	@userActive			NVARCHAR(50)
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;
	
	DECLARE @hinhThucQuangCaoId	INT = 0,
			@tenHinhThucQuangCao NVARCHAR(50) = '',
			@donViTinh	NVARCHAR(50) = N'Gói',
			@soLuong	INT = 1
			
	SET @hinhThucQuangCaoId = 27;
	SET @tenHinhThucQuangCao = 'Google Adsense';

    INSERT INTO ThucChayDaTinhOther
		([ThucChayDaTinhOtherID]
           ,[DmSanPhamREF]
           ,[TenSanPham]
           ,[DmHinhThucQuangCao]
           ,[TenHinhThucQuangCao]
           ,[DonViTinh]
           ,[SoLuongThucChay]
           ,[ThanhTienThucChay]
           ,[GhiChu]
           ,[NgayThucHien]
           ,[CreatedAt]
           ,[CreatedBy]
           ,[LastModifiedAt]
           ,[LastModifiedBy]
           ,[Recordstatus]
           ,[DeletedStatus])
		VALUES
           (NEWID()
           ,@sanPhamId
           ,@tenSanPham
           ,@hinhThucQuangCaoId
           ,@tenHinhThucQuangCao
           ,@donViTinh
           ,@soLuong
           ,@tienThucChay
           ,@ghiChu
           ,CONVERT(DATE,GETDATE())
           ,GETDATE()
           ,@userActive
           ,GETDATE()
           ,@userActive
           ,0
           ,0)
END

```
