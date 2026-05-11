# Stored Procedure: `Gen_GetParameter_NhanSuQuaTrinhCongTac`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-10-09 17:34:07.437000
- **Ngày sửa cuối**: 2014-11-19 12:16:49.860000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[Gen_GetParameter_NhanSuQuaTrinhCongTac] 	
As 	
Begin 	
Select 	
(Select Isnull(Max([LastModifiedAt]),'2010-01-01') from [dbo].[NhanSuQuaTrinhCongTac] Where 1=1  and DeletedStatus <> 1) As 'NgaySua'	
End

```
