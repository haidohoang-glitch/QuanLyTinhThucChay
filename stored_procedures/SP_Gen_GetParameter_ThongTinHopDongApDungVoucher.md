# Stored Procedure: `Gen_GetParameter_ThongTinHopDongApDungVoucher`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2016-01-08 10:40:02.040000
- **Ngày sửa cuối**: 2016-01-08 10:40:02.040000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
Create PROCEDURE [dbo].[Gen_GetParameter_ThongTinHopDongApDungVoucher] 	
As 	
Begin 	
Select 	
(Select Isnull(Max([LastModifiedAt]),'2010-01-01') from [dbo].[ThongTinHopDongApDungVoucher] Where 1=1  and DeletedStatus <> 1) As 'NgaySua'	
End
```
