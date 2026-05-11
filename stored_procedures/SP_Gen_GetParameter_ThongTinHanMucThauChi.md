# Stored Procedure: `Gen_GetParameter_ThongTinHanMucThauChi`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2016-03-14 18:20:15.573000
- **Ngày sửa cuối**: 2016-03-14 18:20:15.573000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
Create PROCEDURE [dbo].[Gen_GetParameter_ThongTinHanMucThauChi] 	
As 	
Begin 	
Select 	
(Select Isnull(Max([LastModifiedAt]),'2010-01-01') from [dbo].[ThongTinHanMucThauChi] Where 1=1  and DeletedStatus <> 1) As 'NgaySua'	
End
```
