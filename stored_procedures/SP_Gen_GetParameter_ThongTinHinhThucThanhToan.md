# Stored Procedure: `Gen_GetParameter_ThongTinHinhThucThanhToan`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2016-05-11 16:53:50.937000
- **Ngày sửa cuối**: 2016-05-11 16:53:50.937000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
Create PROCEDURE [dbo].[Gen_GetParameter_ThongTinHinhThucThanhToan] 	
As 	
Begin 	
Select 	
(Select Isnull(Max([LastModifiedAt]),'2010-01-01') from [dbo].[ThongTinHinhThucThanhToan] Where 1=1  and DeletedStatus <> 1) As 'NgaySua'	
End
```
