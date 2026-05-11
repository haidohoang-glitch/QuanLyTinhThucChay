# Stored Procedure: `Gen_GetParameter_ThongTinTienVe`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-09-19 17:22:12.503000
- **Ngày sửa cuối**: 2014-11-19 12:16:49.227000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[Gen_GetParameter_ThongTinTienVe] 	
As 	
Begin 	
Select 	
(Select Isnull(Max([LastModifiedAt]),'2010-01-01') from [dbo].[ThongTinTienVe] Where 1=1  and DeletedStatus <> 1) As 'NgaySua'	
End

```
