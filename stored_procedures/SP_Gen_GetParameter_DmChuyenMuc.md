# Stored Procedure: `Gen_GetParameter_DmChuyenMuc`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-09-03 15:57:26.167000
- **Ngày sửa cuối**: 2014-11-19 12:16:51.047000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[Gen_GetParameter_DmChuyenMuc] 	
As 	
Begin 	
Select 	
(Select Isnull(Max([LastModifiedAt]),'2010-01-01') from [dbo].[DmChuyenMuc] Where 1=1  and DeletedStatus <> 1) As 'NgaySua'	
End

```
