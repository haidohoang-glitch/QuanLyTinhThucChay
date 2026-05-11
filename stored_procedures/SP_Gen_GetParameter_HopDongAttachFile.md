# Stored Procedure: `Gen_GetParameter_HopDongAttachFile`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-08-26 09:42:27.050000
- **Ngày sửa cuối**: 2014-11-19 12:16:51.247000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[Gen_GetParameter_HopDongAttachFile] 	
As 	
Begin 	
Select 	
(Select Isnull(Max([LastModifiedAt]),'2010-01-01') from [dbo].[HopDongAttachFile] Where 1=1  and DeletedStatus <> 1) As 'NgaySua'	
End

```
