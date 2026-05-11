# Function: `Get_NhanHangCha`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2016-03-18 11:25:21.840000
- **Ngày sửa cuối**: 2018-11-07 15:48:27.767000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `nvarchar(510)` | Yes |
| `@NhanHangID` | `int(4)` | No |

## Definition (Source Code)

```sql

CREATE FUNCTION [dbo].[Get_NhanHangCha] ( @NhanHangID INT )
RETURNS NVARCHAR(255)
    BEGIN
        DECLARE @NhanChaID INT
		DECLARE @Temp INT
        DECLARE @TenNhanHangCha NVARCHAR(255)
        SELECT  @NhanChaID = ISNULL(NhanHangCha, -1)
        FROM    [192.168.23.217].BRAND.dbo.DmNhanHang
        WHERE   DmNhanHangID = @NhanHangID
        IF @NhanChaID = -1 
            BEGIN	
            		SELECT @TenNhanHangCha= dnh.TenNhanHang
            		FROM[192.168.23.217].BRAND.dbo.DmNhanHang dnh WHERE dnh.DmNhanHangID=@NhanHangID	
            	  
                RETURN @TenNhanHangCha
            END
        ELSE 
            BEGIN
				SELECT  @Temp = NhanHangCha							
				FROM    [192.168.23.217].BRAND.dbo.DmNhanHang
				WHERE   DmNhanHangID = @NhanHangID
            
                WHILE @Temp > 0 
                    BEGIN
						
						SELECT  @TenNhanHangCha = TenNhanHang
						FROM  [192.168.23.217].BRAND.dbo.DmNhanHang
						WHERE   DmNhanHangID = @Temp
						
						SELECT  @Temp = ISNULL(NhanHangCha, -1)								
						FROM   [192.168.23.217].BRAND.dbo.DmNhanHang
						WHERE   DmNhanHangID = @Temp
						--SELECT	@TenNhanHangCha= dnh.TenNhanHang
      --      			FROM DmNhanHang dnh WHERE dnh.DmNhanHangID=@Temp	
                    END	
            END
					SELECT	@TenNhanHangCha= dnh.TenNhanHang
            			FROM[192.168.23.217].BRAND.dbo.DmNhanHang dnh WHERE dnh.DmNhanHangID=@Temp	
        RETURN @TenNhanHangCha
	
    END

```
