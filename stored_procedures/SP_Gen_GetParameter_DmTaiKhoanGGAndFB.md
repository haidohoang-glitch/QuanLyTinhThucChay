# Stored Procedure: `Gen_GetParameter_DmTaiKhoanGGAndFB`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2015-03-05 11:28:20.567000
- **Ngày sửa cuối**: 2015-03-05 11:28:20.567000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
Create PROCEDURE [dbo].[Gen_GetParameter_DmTaiKhoanGGAndFB] 	
As 	
Begin 	
Select 	
(Select Isnull(Max([LastModifiedAt]),'2010-01-01') from [dbo].[DmTaiKhoanGGAndFB] Where 1=1 ) As 'NgaySua'	
End
```
