# Stored Procedure: `Gen_GetParameter_ThongTinTienVeLog`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-09-19 17:26:07.077000
- **Ngày sửa cuối**: 2014-11-19 12:16:49.183000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[Gen_GetParameter_ThongTinTienVeLog] 	
As 	
Begin 	
Select 	
(Select Isnull(Max([ThoiGianLog]),'2010-01-01') from [dbo].[ThongTinTienVeLog] Where 1=1  and DeletedStatus <> 1) As 'NgaySua'	
End

```
