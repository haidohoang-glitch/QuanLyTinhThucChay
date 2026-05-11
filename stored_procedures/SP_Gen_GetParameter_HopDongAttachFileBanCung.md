# Stored Procedure: `Gen_GetParameter_HopDongAttachFileBanCung`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-09-19 17:26:56.460000
- **Ngày sửa cuối**: 2014-11-19 12:16:51.230000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[Gen_GetParameter_HopDongAttachFileBanCung] 	
As 	
Begin 	
Select 	
(Select Isnull(Max([LastModifiedAt]),'2010-01-01') from [dbo].[HopDongAttachFileBanCung] Where 1=1  and DeletedStatus <> 1) As 'NgaySua'	
End

```
