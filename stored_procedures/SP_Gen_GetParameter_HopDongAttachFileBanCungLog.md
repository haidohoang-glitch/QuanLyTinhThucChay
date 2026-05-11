# Stored Procedure: `Gen_GetParameter_HopDongAttachFileBanCungLog`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-09-20 10:37:33.907000
- **Ngày sửa cuối**: 2014-11-19 12:16:51.213000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[Gen_GetParameter_HopDongAttachFileBanCungLog] 	
As 	
Begin 	
Select 	
(Select Isnull(Max([ThoiGianLog]),'2010-01-01') from [dbo].[HopDongAttachFileBanCungLog] Where 1=1  and DeletedStatus <> 1) As 'NgaySua'	
End

```
