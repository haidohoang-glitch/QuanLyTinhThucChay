# Stored Procedure: `Gen_GetParameter_ThucChayHopDongChiTiet`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-08-28 14:08:37.390000
- **Ngày sửa cuối**: 2014-11-19 12:16:50.697000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[Gen_GetParameter_ThucChayHopDongChiTiet] 	
As 	
Begin 	
Select 	
(Select Isnull(Max([LastModifiedAt]),'2010-01-01') from [dbo].[ThucChayHopDongChiTiet] Where 1=1  and DeletedStatus <> 1) As 'NgaySua'	
End

```
