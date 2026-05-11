# Stored Procedure: `ThucChayAdmarketUser_NhanHang_Insert_dev20160926`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2016-09-26 15:51:36.293000
- **Ngày sửa cuối**: 2016-09-26 15:56:49.510000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@DmSanPhamREF` | `int(4)` | No |
| `@TenSanPham` | `nvarchar(100)` | No |
| `@domain` | `nvarchar(100)` | No |
| `@ttc` | `int(4)` | No |
| `@ttv` | `int(4)` | No |
| `@money` | `float(8)` | No |
| `@pro` | `float(8)` | No |
| `@NgayThucHien` | `datetime(8)` | No |
| `@IsNoiBo` | `int(4)` | No |
| `@username` | `nvarchar(100)` | No |
| `@userid` | `int(4)` | No |
| `@DmNhanHangREF` | `int(4)` | No |
| `@TenNhanHang` | `nvarchar(400)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		Doannv
-- Create date: 2014-06-02
-- Description:	Insert ThucChayAdmarketUsers
-- =============================================



CREATE PROCEDURE [dbo].[ThucChayAdmarketUser_NhanHang_Insert_dev20160926] 
	-- Add the parameters for the stored procedure here
	@DmSanPhamREF	INT,
	@TenSanPham		NVARCHAR(50),
	@domain	NVARCHAR(50),
	@ttc	INT,
	@ttv	INT,
	@money	FLOAT,
	@pro	FLOAT,
	@NgayThucHien	DATETIME,
	@IsNoiBo int,
	@username NVARCHAR(50),
	@userid INT,
	@DmNhanHangREF INT ,
	@TenNhanHang NVARCHAR(200)

AS
BEGIN
	DECLARE @DmNhanHangThayDoi INT, @TenNhanHangThayDoi NVARCHAR(400)


	SELECT @DmNhanHangThayDoi = nh.DmNhanHangThayDoiID, @TenNhanHangThayDoi = nhtd.TenNhanHang
	FROM [ASD-SQLSVR_UUTP].ABM_Data_Release.dbo.DmNhanHang nh
	INNER JOIN dbo.DmNhanHang nhtd ON nh.DmNhanHangThayDoiID = nhtd.DmNhanHangID
	WHERE nh.DmNhanHangID = @DmNhanHangREF
	AND nh.DmNhanHangThayDoiID <>0
	AND nh.DeletedStatus = 1

	IF(ISNULL(@DmNhanHangThayDoi,0) <>0)
	BEGIN
		SET @DmNhanHangREF = @DmNhanHangThayDoi
		SET @TenNhanHang = @TenNhanHangThayDoi
	END
	--1. XAC DINH XEM NHAN HANG NAY DA DUOC CHUAN HOA CHUA
	--2. NEU DA CHUAN HOA THI LAY THONG TIN NHAN HANG THAY DOI VA CAP NHAT LAI THONG TIN NHAN HANG
	INSERT INTO [dbo].ThucChayAdmarketUser_NhanHang
           ([DmSanPhamREF]
           ,[username]
           ,[TenSanPham]
           ,[Domain]
           ,[ttc]
           ,[ttv]
           ,[money]
           ,[pro]
           ,[IsNoiBo]
           ,[NgayThucHien]
           ,[CreatedAt]
           ,[CreatedBy]
           ,[LastModifedAt]
           ,[LastModifiedBy]
           ,userid
           ,DmNhanHangREF
           ,TenNhanHang
           )
     VALUES
           (
				@DmSanPhamREF
				,@username
				,@TenSanPham
				,@domain
				,@ttc
				,@ttv
				,@money
				,@pro
				,@IsNoiBo
				,@NgayThucHien
				,GETDATE()
				,'asd'
				,GETDATE()
				,'asd'	
				,@userid
				,@DmNhanHangREF
				,@TenNhanHang
           )
END

```
