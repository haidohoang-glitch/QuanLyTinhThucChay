# Stored Procedure: `Gen_GetParameter_ThongTinHoaDon_KhongSoHopDong`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2015-06-09 10:18:35.480000
- **Ngày sửa cuối**: 2015-06-09 10:18:35.480000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
Create PROCEDURE [dbo].[Gen_GetParameter_ThongTinHoaDon_KhongSoHopDong] 	
As 	
Begin 	
Select 	
(Select Isnull(Max([LastModifiedAt]),'2010-01-01') from [dbo].[ThongTinHoaDon_KhongSoHopDong] Where 1=1  and DeletedStatus <> 1) As 'NgaySua'	
End
```
