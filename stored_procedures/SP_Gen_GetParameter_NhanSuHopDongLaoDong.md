# Stored Procedure: `Gen_GetParameter_NhanSuHopDongLaoDong`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-10-07 16:36:49.103000
- **Ngày sửa cuối**: 2014-11-19 12:16:49.893000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[Gen_GetParameter_NhanSuHopDongLaoDong] 	
As 	
Begin 	
Select 	
(Select Isnull(Max([LastModifiedAt]),'2010-01-01') from [dbo].[NhanSuHopDongLaoDong] Where 1=1  and DeletedStatus <> 1) As 'NgaySua'	
End

```
