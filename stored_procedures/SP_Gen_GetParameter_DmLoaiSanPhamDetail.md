# Stored Procedure: `Gen_GetParameter_DmLoaiSanPhamDetail`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-08-26 09:48:26.560000
- **Ngày sửa cuối**: 2014-11-19 12:16:52.733000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[Gen_GetParameter_DmLoaiSanPhamDetail] 	
As 	
Begin 	
Select 	
(Select Isnull(Max([LastModifiedAt]),'2010-01-01') from [dbo].[DmLoaiSanPhamDetail] Where 1=1  and DeletedStatus <> 1) As 'NgaySua'	
End

```
