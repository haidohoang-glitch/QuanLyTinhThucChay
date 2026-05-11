# Stored Procedure: `Gen_InsertOrUpdate_ThucChayCPR_v1`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-06-19 14:59:35.407000
- **Ngày sửa cuối**: 2017-08-31 16:46:08.743000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@TypeProduct` | `int(4)` | No |

## Definition (Source Code)

```sql
/*
EXEC [dbo].[Gen_InsertOrUpdate_ThucChayCPR_v1] 18
*/
CREATE PROCEDURE [dbo].[Gen_InsertOrUpdate_ThucChayCPR_v1]
	@TypeProduct INT
	
AS
BEGIN
	DECLARE @ThucChayCPR
		TABLE(
			bannerid INT,
			uvNgay INT,
			uv INT,
			typeproduct INT,
			ProductName NVARCHAR(200),
			NgayThucHien DATETIME,
			ThoiGianTao DATETIME,
			uvhour NVARCHAR(1000)
		)
	DECLARE @SQL NVARCHAR(MAX) = '', @DauNhay NVARCHAR(100) = '"', @NgayThucHien DATETIME
	DECLARE @UvNgayTruoc INT = 0, @v_UvNgay INT = 0
	,@v_ThoiGianTao DATETIME =GETDATE()
	
	--SET @NgayThucHien =	(
	--		SELECT Dateadd(day,1,Isnull(Max([NgayThucHien]),'2017-08-01')) 
	--		FROM [dbo].[ThucChayCPR] 
	--		WHERE 1=1 AND typeproduct = @TypeProduct
	--	)
	SET @NgayThucHien =	CONVERT(DATE,DATEADD(DAY,-1,GETDATE()))
		
		--XOA DU LIEU CUA NGAY TRUOC KHI LAY
	DELETE  FROM [ThucChayCPR]
	WHERE NgayThucHien = @NgayThucHien
	AND TypeProduct = @TypeProduct

	SET @SQL = 'CALL SelectThucChay_UV_ASD_By_date ('+ @DauNhay + CONVERT(NVARCHAR(20), @NgayThucHien, 120) + @DauNhay + ','  + CONVERT(NVARCHAR(20), @TypeProduct)  + ' );'
	SET @SQL = 
		'Select
    		hdct.*
		from openquery([ReportingDB],''' + @SQL + ''') hdct'
	--PRINT @SQL

	INSERT INTO @ThucChayCPR
	        ( bannerid ,
	          uvNgay ,
	          uv ,
	          typeproduct ,
	          ProductName ,
	          NgayThucHien ,
	          ThoiGianTao ,
	          uvhour
	        )
	EXECUTE
	  (
		@SQL
	  )

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
   SELECT bannerid,
		uvNgay,
		uv,
		typeproduct,
		ProductName,
		NgayThucHien,
		ThoiGianTao,
		uvhour ,
		0,
		0
		FROM @ThucChayCPR


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
	SELECT bannerid,
		(uv -
		ISNULL((
			SELECT TOP 1 uv FROM ThucChayCPR
			WHERE BannerID = t.bannerid
			AND NgayThucHien <@NgayThucHien
			AND typeproduct = t.typeproduct
			ORDER BY NgayThucHien desc
		),0)),
		uv,
		typeproduct,
		ProductName,
		NgayThucHien,
		GETDATE(),
		uvhour FROM @ThucChayCPR t

END
	
```
