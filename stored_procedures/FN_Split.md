# Function: `Split`

- **Loại**: SQL_TABLE_VALUED_FUNCTION
- **Ngày tạo**: 2013-06-18 16:58:31.947000
- **Ngày sửa cuối**: 2015-01-28 15:37:28.140000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@String` | `varchar` | No |
| `@Delimiter` | `char(1)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE FUNCTION [dbo].[Split](@String varchar(max), @Delimiter char(1))       
returns @temptable TABLE (items varchar(max))       
as       
begin       
    declare @idx int       
    declare @slice varchar(max)       

    select @idx = 1       
        if len(@String)<1 or @String is null  return       

    while @idx!= 0       
    begin       
        set @idx = charindex(@Delimiter,@String)       
        if @idx!=0       
            set @slice = left(@String,@idx - 1)       
        else       
            set @slice = @String       

        if(len(@slice)>0)  
            insert into @temptable(Items) values(@slice)       

        set @String = right(@String,len(@String) - @idx)       
        if len(@String) = 0 break       
    end   
return       
end

```
