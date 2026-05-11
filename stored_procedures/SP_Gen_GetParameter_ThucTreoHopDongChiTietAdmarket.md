# Stored Procedure: `Gen_GetParameter_ThucTreoHopDongChiTietAdmarket`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-09-08 15:27:13.790000
- **Ngày sửa cuối**: 2014-11-19 12:16:50.570000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[Gen_GetParameter_ThucTreoHopDongChiTietAdmarket] 	
As 	
Begin 	
Select 	
(Select Isnull(Max([LastModifiedAt]),'2010-01-01') from [dbo].[ThucTreoHopDongChiTietAdmarket] Where 1=1  and DeletedStatus <> 1) As 'NgaySua'	
End

```
