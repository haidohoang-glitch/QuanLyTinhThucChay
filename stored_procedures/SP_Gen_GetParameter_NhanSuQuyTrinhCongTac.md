# Stored Procedure: `Gen_GetParameter_NhanSuQuyTrinhCongTac`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-10-09 16:29:24.647000
- **Ngày sửa cuối**: 2014-11-19 12:16:49.710000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[Gen_GetParameter_NhanSuQuyTrinhCongTac] 	
As 	
Begin 	
Select 	
(Select Isnull(Max([LastModifiedAt]),'2010-01-01') from [dbo].[NhanSuQuyTrinhCongTac] Where 1=1  and DeletedStatus <> 1) As 'NgaySua'	
End

```
