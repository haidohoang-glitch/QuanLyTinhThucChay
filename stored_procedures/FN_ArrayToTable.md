# Function: `ArrayToTable`

- **Loại**: SQL_INLINE_TABLE_VALUED_FUNCTION
- **Ngày tạo**: 2013-05-23 08:52:30.920000
- **Ngày sửa cuối**: 2014-10-14 10:39:38.047000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@TheArray` | `xml` | No |

## Definition (Source Code)

```sql
create FUNCTION [dbo].[ArrayToTable]
(  
@TheArray XML
)
RETURNS TABLE
AS
RETURN
(
SELECT   x.y.value('seqno[1]', 'INT') AS [seqno],
        x.y.value('item[1]', 'VARCHAR(200)') AS [item]
FROM     @TheArray.nodes('//stringarray/element') AS x (y)
)

```
