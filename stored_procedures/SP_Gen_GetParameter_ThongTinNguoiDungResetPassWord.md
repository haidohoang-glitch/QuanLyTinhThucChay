# Stored Procedure: `Gen_GetParameter_ThongTinNguoiDungResetPassWord`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-10-07 16:32:07.997000
- **Ngày sửa cuối**: 2014-11-19 12:16:49.250000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[Gen_GetParameter_ThongTinNguoiDungResetPassWord] 	
As 	
Begin 	
Select 	
(Select Isnull(Max([LastModifiedAt]),'2010-01-01') from [dbo].[ThongTinNguoiDungResetPassWord] Where 1=1  and DeletedStatus <> 1) As 'NgaySua'	
End

```
