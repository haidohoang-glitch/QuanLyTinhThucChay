# Function: `fn_getTableTime`

- **Loại**: SQL_TABLE_VALUED_FUNCTION
- **Ngày tạo**: 2015-03-27 17:42:58.270000
- **Ngày sửa cuối**: 2015-03-27 17:42:58.270000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@FromDate` | `datetime(8)` | No |
| `@ToDate` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
--SELECT * from [dbo].[fn_getTableTime]('2013-01-01','2014-09-15')
CREATE FUNCTION [dbo].[fn_getTableTime]
(	
	-- Add the parameters for the function here
	@FromDate DATETIME,
	@ToDate DATETIME
)
RETURNS @TableTime TABLE 
(
	    FromDate DATETIME,
		Todate DATETIME,
		isNam INT,
		isQuy INT,
		isThang INT,
		isNgay INT ,
		Nam INT,
		Quy INT,
		Thang INT
	)
AS
BEGIN
	WHILE @FromDate < @Todate
BEGIN
	--Kiểm tra khoảng năm
	IF(MONTH(@FromDate)=1 AND DAY(@FromDate) = 1 AND  DATEADD(DAY,-1,DATEADD(yyyy,1,@FromDate)) <=@todate )
	BEGIN		
		INSERT INTO @TableTime
		(
			FromDate,
			Todate,
			isNam,
			isQuy,
			isThang,
			isNgay,
			Nam,
			Quy,
			Thang
		)
		VALUES
		(
			@FromDate,
			CAST(DATEADD(DAY,-1,DATEADD(yyyy,1,@FromDate)) AS DATETIME),
			1,
			0,
			0,
			0,
			YEAR(@FromDate),
			-1,
			-1
		)
		set @FromDate = DATEADD(yyyy,1,@FromDate)
	END
	ELSE
	BEGIN
		--Kiểm tra Quý
			IF(
				CAST(DATEADD(DAY,-1,DATEADD(QQ,1,@FromDate)) AS DATETIME)< @Todate AND 
				 DAY(@FromDate) = 1 AND
				(
				(MONTH(@FromDate)=1 ) OR 
				(MONTH(@FromDate)=4 ) OR 
				(MONTH(@FromDate)=7 ) OR 
				(MONTH(@FromDate)=10)
				)
				
			  )
			BEGIN
				INSERT INTO @TableTime
					(
						FromDate,
						Todate,
						isNam,
						isQuy,
						isThang,
						isNgay,
						Nam,
						Quy,
						Thang
					)
					VALUES
					(
						@FromDate,
						CAST(DATEADD(DAY,-1,DATEADD(QQ,1,@FromDate)) AS DATETIME),
						0,
						1,
						0,
						0,
						YEAR(@FromDate),
						DATEPART(QQ,@FromDate),
						-1
					)
				SET @FromDate = DATEADD(QQ,1,@FromDate)
			END
			ELSE
			BEGIN
				--Kiểm tra tháng
					IF(DAY(@FromDate) =1 AND DATEDIFF(MONTH,@FromDate,DATEADD(DAY,1,@ToDate)) >=1)
					BEGIN
					INSERT INTO @TableTime
					(
						FromDate,
						Todate,
						isNam,
						isQuy,
						isThang,
						isNgay,
						Nam,
						Quy,
						Thang
					)
					VALUES
					(
						@FromDate,
						CAST(DATEADD(DAY,-1,DATEADD(MONTH,1,@FromDate)) AS DATETIME),
						0,
						0,
						1,
						0,
						YEAR(@FromDate),
						-1,
						MONTH(@FromDate)
					)
					SET @FromDate = DATEADD(MONTH,1,@FromDate)
					END	
				ELSE
					--Chuyển sang đầu tháng gần nhất để tiếp tục duyệt
					IF (Dateadd(Month,1,DATEADD(DAY,-DAY(@FromDate) +1,@FromDate))<= @Todate)
					BEGIN
						INSERT INTO @TableTime
					(
						FromDate,
						Todate,
						isNam,
						isQuy,
						isThang,
						isNgay,
						Nam,
						Quy,
						Thang
					)
					VALUES
					(
						@FromDate,
						Dateadd(Month,1,DATEADD(DAY,-DAY(@FromDate) + 1,@FromDate)),
						0,
						0,
						0,
						1,
						-1,
						-1,
						-1
					)
					END
					ELSE
						--Khoảng thời gian không đủ tháng
					 BEGIN
						
					INSERT INTO @TableTime
					(
						FromDate,
						Todate,
						isNam,
						isQuy,
						isThang,
						isNgay,
						Nam,
						Quy,
						Thang
					)
					VALUES
					(
						@FromDate,
						@Todate,
						0,
						0,
						0,
						1,
						-1,
						-1,
						-1
					)
						set @FromDate = @ToDate
				   end
				END
		END
END
RETURN 
END

```
