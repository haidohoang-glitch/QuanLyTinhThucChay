# Stored Procedure: `Gen_GetParameter_ThucChayHopDongChiTietPR`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-09-08 15:25:38.590000
- **Ngày sửa cuối**: 2014-11-19 12:17:54.310000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[Gen_GetParameter_ThucChayHopDongChiTietPR] 	
As 	
Begin 	
Select 	
(Select Isnull(Max([LastModifiedAt]),'2010-01-01') from [dbo].[ThucChayHopDongChiTietPR] Where 1=1  and DeletedStatus <> 1) As 'NgaySua'	
End

```
