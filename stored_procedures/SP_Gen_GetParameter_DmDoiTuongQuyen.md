# Stored Procedure: `Gen_GetParameter_DmDoiTuongQuyen`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-10-07 16:32:23.300000
- **Ngày sửa cuối**: 2014-11-19 12:16:51.030000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[Gen_GetParameter_DmDoiTuongQuyen] 	
As 	
Begin 	
Select 	
(Select Isnull(Max([LastModifiedAt]),'2010-01-01') from [dbo].[DmDoiTuongQuyen] Where 1=1  and DeletedStatus <> 1) As 'NgaySua'	
End

```
