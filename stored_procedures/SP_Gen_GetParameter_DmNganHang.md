# Stored Procedure: `Gen_GetParameter_DmNganHang`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-09-26 16:39:38.277000
- **Ngày sửa cuối**: 2014-11-19 12:16:52.697000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[Gen_GetParameter_DmNganHang] 	
As 	
Begin 	
Select 	
(Select Isnull(Max([LastModifiedAt]),'2010-01-01') from [dbo].[DmNganHang] Where 1=1  and DeletedStatus <> 1) As 'NgaySua'	
End

```
