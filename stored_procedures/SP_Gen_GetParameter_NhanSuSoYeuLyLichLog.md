# Stored Procedure: `Gen_GetParameter_NhanSuSoYeuLyLichLog`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-10-07 16:37:37.970000
- **Ngày sửa cuối**: 2014-11-19 12:16:49.640000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[Gen_GetParameter_NhanSuSoYeuLyLichLog] 	
As 	
Begin 	
Select 	
(Select Isnull(Max([ThoiGianLog]),'2010-01-01') from [dbo].[NhanSuSoYeuLyLichLog] Where 1=1  and DeletedStatus <> 1) As 'NgaySua'	
End

```
