# Function: `GetMaLinkBai`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2015-01-28 12:38:04.443000
- **Ngày sửa cuối**: 2015-01-28 16:09:51.217000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `varchar(50)` | Yes |
| `@Link` | `varchar(500)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date, ,>
-- Description:	<Description, ,>
-- =============================================
CREATE FUNCTION GetMaLinkBai 
(
	-- Add the parameters for the function here
	@Link VARCHAR(500)
)
RETURNS VARCHAR(50)
AS
BEGIN

DECLARE @Result VARCHAR(500), @Result1 VARCHAR(500), @ResultFinal VARCHAR(500)
DECLARE @RecordCount INT

----'http://vneconomy.vn/20140522085054926P19C9915/tang-1-chieu-bay-noi-dia-cho-chu-the-dong-thuong-hieu-vna-vpbank.htm'

--SET @Link = 'http://vneconomy.vn/20140522085054926P19C9915/tang-1-chieu-bay-noi-dia-cho-chu-the-dong-thuong-hieu-vna-vpbank.htm'--'http://giadinh.net.vn/dep/uu-diem-noi-bat-cua-kem-tri-nam-sac-ngoc-khang-20140917053511142.htm'

SET @Link = RTRIM(@Link)
SET @Link = LTRIM(@Link)
SET @Result = REPLACE(@Link,'http://','')
SET @Result = REPLACE(@Result,'https://','')
SET @Result = REPLACE(@Result,'.htm','')
SET @Result = REPLACE(@Result,'.html','')
SET @Result = REPLACE(@Result,'.chn','')

SET @Result1 = @Result

set @RecordCount = (SELECT COUNT(*) FROM [dbo].[Split](@Result,'/')
				WHERE
				items LIKE '%2014%')

IF @RecordCount =1 
BEGIN
	SET @Result = (SELECT items FROM [dbo].[Split](@Result,'/')
					WHERE
					items LIKE '%2014%')

	set @RecordCount = (SELECT COUNT(*) FROM [dbo].[Split](@Result,'-')
				WHERE
				items LIKE '%2014%'
				and ISNUMERIC(items) = 1			
				)
				
	IF @RecordCount =1 
		BEGIN
			SET @Result = (SELECT items FROM [dbo].[Split](@Result,'-')
							WHERE
							items LIKE '%2014%'
							and ISNUMERIC(items) = 1				
							)
							
			if len(@Result) >= 17
				SET @Result = SUBSTRING(@Result,1,17)

			IF(len(@Result)>=7)
				set @ResultFinal = @Result		
		END
	ELSE
		--Is Dan Tri
		BEGIN
			set @RecordCount = (SELECT COUNT(*) FROM [dbo].[Split](@Result1,'-')
							WHERE
							ISNUMERIC(items) = 1
							and len(items) > 4
							)

			IF @RecordCount =1 			
				set @ResultFinal = (SELECT items FROM [dbo].[Split](@Result1,'-')
							WHERE
							ISNUMERIC(items) = 1	
							and len(items) > 4)
		END
END

IF @ResultFinal IS NULL
	BEGIN
		set @RecordCount = (SELECT COUNT(*) FROM [dbo].[Split](@Result1,'/')
						WHERE
						ISNUMERIC(items) = 1
						and len(items) > 4
						)

		IF @RecordCount =1 			
			set @ResultFinal = (SELECT items FROM [dbo].[Split](@Result1,'/')
						WHERE
						ISNUMERIC(items) = 1	
						and len(items) > 4)
		ELSE
			BEGIN
				set @RecordCount = (SELECT COUNT(*) FROM [dbo].[Split](@Result1,'/')
								WHERE
								ISNUMERIC(SUBSTRING(items,CHARINDEX('-', items)+1,len(items))) = 1
								and len(items) > 4
								)

				IF @RecordCount =1 			
					set @ResultFinal = (SELECT SUBSTRING(items,CHARINDEX('-', items)+1,len(items)) FROM [dbo].[Split](@Result1,'/')
								WHERE
								ISNUMERIC(SUBSTRING(items,CHARINDEX('-', items)+1,len(items))) = 1	
								and len(items) > 4)	
				ELSE
					BEGIN
						set @RecordCount = (SELECT COUNT(*) FROM [dbo].[Split](@Result1,'/') 
										WHERE
										1=1
										and len(items) > 4
										AND 
										ISNUMERIC(substring(items,dbo.GetLastCharIndex(items, '-')+1,LEN(items)))  = 1
										)
						IF @RecordCount =1 			
							set @ResultFinal = (SELECT substring(items,dbo.GetLastCharIndex(items, '-')+1,LEN(items))  FROM [dbo].[Split](@Result1,'/') 
										WHERE
										1=1	
										and len(items) > 4
										AND 
										ISNUMERIC(substring(items,dbo.GetLastCharIndex(items, '-')+1,LEN(items)))  = 1	
										)		
						ELSE
							BEGIN
								set @RecordCount = (SELECT COUNT(*) FROM [dbo].[Split](@Result1,'/') 
												WHERE
												1=1
												and len(items) > 4
												AND 
												ISNUMERIC(
													dbo.GetNumberFromString(
																substring(items,dbo.GetLastCharIndex(items, '-')+1,LEN(items))
																			)
															)  = 1
												)
								IF @RecordCount =1 			
									set @ResultFinal = (SELECT dbo.GetNumberFromString(substring(items,dbo.GetLastCharIndex(items, '-')+1,LEN(items)))  FROM [dbo].[Split](@Result1,'/') 
												WHERE
												1=1	
												and len(items) > 4
												AND 
												ISNUMERIC(
													dbo.GetNumberFromString(
																substring(items,dbo.GetLastCharIndex(items, '-')+1,LEN(items))
																			)
															)  = 1	
												)	
								ELSE
									BEGIN
										set @RecordCount = (SELECT COUNT(*) FROM [dbo].[Split](@Result1,'/') 
														WHERE
														1=1
														and len(items) > 4
														AND 
														ISNUMERIC(dbo.GetNumberInString(items))  = 1
														)
										IF @RecordCount =1 			
											set @ResultFinal = (SELECT dbo.GetNumberInString(items)  FROM [dbo].[Split](@Result1,'/') 
														WHERE
														1=1	
														and len(items) > 4
														AND 
														ISNUMERIC(dbo.GetNumberInString(items))  = 1
														)	
										ELSE
											BEGIN
												set @RecordCount = (SELECT COUNT(*) FROM [dbo].[Split](@Result1,'/') 
																WHERE
																1=1
																and len(items) > 4
																AND 
																ISNUMERIC(dbo.GetNumberFromString(items))  = 1
																)
												IF @RecordCount =1 			
													set @ResultFinal = (SELECT dbo.GetNumberFromString(items)  FROM [dbo].[Split](@Result1,'/') 
																WHERE
																1=1	
																and len(items) > 4
																AND 
																ISNUMERIC(dbo.GetNumberFromString(items))  = 1
																)												
											END																									
									END																					
							END																								
					END			
			END
	END

	-- Return the result of the function
	RETURN @ResultFinal

END

```
