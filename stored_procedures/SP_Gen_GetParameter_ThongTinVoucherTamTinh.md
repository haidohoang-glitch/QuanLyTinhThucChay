# Stored Procedure: `Gen_GetParameter_ThongTinVoucherTamTinh`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2016-01-08 10:16:25.810000
- **Ngày sửa cuối**: 2016-01-08 10:16:25.810000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
Create PROCEDURE [dbo].[Gen_GetParameter_ThongTinVoucherTamTinh] 	
As 	
Begin 	
Select 	
(Select Isnull(Max([LastModifiedAt]),'2010-01-01') from [dbo].[ThongTinVoucherTamTinh] Where 1=1 ) As 'NgaySua'	
End
```
