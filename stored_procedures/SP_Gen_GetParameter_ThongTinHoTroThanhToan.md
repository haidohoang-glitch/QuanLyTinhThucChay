# Stored Procedure: `Gen_GetParameter_ThongTinHoTroThanhToan`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2016-03-14 18:19:41.957000
- **Ngày sửa cuối**: 2016-03-14 18:19:41.957000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
Create PROCEDURE [dbo].[Gen_GetParameter_ThongTinHoTroThanhToan] 	
As 	
Begin 	
Select 	
(Select Isnull(Max([LastModifiedAt]),'2010-01-01') from [dbo].[ThongTinHoTroThanhToan] Where 1=1  and DeletedStatus <> 1) As 'NgaySua'	
End
```
