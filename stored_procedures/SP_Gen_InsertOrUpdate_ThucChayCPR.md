# Stored Procedure: `Gen_InsertOrUpdate_ThucChayCPR`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2015-08-31 17:19:01.663000
- **Ngày sửa cuối**: 2016-09-16 17:15:50.463000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@BannerID` | `int(4)` | No |
| `@UvNgay` | `int(4)` | No |
| `@UV` | `bigint(8)` | No |
| `@TypeProduct` | `int(4)` | No |
| `@ProductName` | `nvarchar(200)` | No |
| `@NgayThucHien` | `datetime(8)` | No |
| `@uvhour` | `text(16)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[Gen_InsertOrUpdate_ThucChayCPR]
	@BannerID INT ,
	@UvNgay INT ,
	@UV BIGINT,
	@TypeProduct INT ,
	@ProductName NVARCHAR(100),
	@NgayThucHien DATETIME,
	--@ThoiGianTao NVARCHAR(100) ,
	@uvhour TEXT
	
AS
BEGIN
	DECLARE @UvNgayTruoc INT = 0, @v_UvNgay INT = 0
	,@v_ThoiGianTao DATETIME =GETDATE()
	
INSERT INTO [dbo].[ThucChayCPR_SYN_Log]
           ([bannerid]
           ,[uvNgay]
           ,[uv]
           ,[typeproduct]
           ,[ProductName]
           ,[NgayThucHien]
           ,[ThoiGianTao]
           ,[uvhour]
           ,[TVDenNgay]
           ,[TCDenNgay])
     VALUES
           (@BannerID
           ,@UvNgay
           ,@UV
           ,@TypeProduct
           ,@ProductName
           ,@NgayThucHien
           ,@v_ThoiGianTao
           ,@uvhour
           ,0
           ,0)


	--GET DU LIEU UV CUA BANNERID NGAY HOM TRUOC
	SET @UvNgayTruoc =
	(
		SELECT TOP 1 uv FROM ThucChayCPR
		WHERE BannerID = @BannerID
		AND NgayThucHien <@NgayThucHien
		ORDER BY NgayThucHien desc
	) 
	SET @UvNgayTruoc = ISNULL(@UvNgayTruoc,0)
	SET @UvNgay = @UV - @UvNgayTruoc
	SET @v_UvNgay = @UvNgay
	
	IF (
	       EXISTS(
	           SELECT *
	           FROM ThucChayCPR
	           WHERE  [BannerID] = @BannerID
	           AND [NgayThucHien] = @NgayThucHien
	       )
	)
	BEGIN
		UPDATE ThucChayCPR
		SET
			uv = @UV,
			uvNgay = @v_UvNgay,
			typeproduct = @TypeProduct,
			ProductName = @ProductName,
			ThoiGianTao = @v_ThoiGianTao,
			uvhour = @uvhour
	    WHERE  [BannerID] = @BannerID
	           AND [NgayThucHien] = @NgayThucHien
	END
	ELSE
		INSERT INTO ThucChayCPR
		(
			bannerid,
			uvNgay,
			uv,
			typeproduct,
			ProductName,
			NgayThucHien,
			ThoiGianTao,
			uvhour
		)
		VALUES
		(
			@BannerID,
			@v_UvNgay,
			@UV,
			@TypeProduct,
			@ProductName,
			@NgayThucHien,
			@v_ThoiGianTao,
			@uvhour
		)

END
	
```
