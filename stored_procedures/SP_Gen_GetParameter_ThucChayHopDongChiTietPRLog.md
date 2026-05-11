# Stored Procedure: `Gen_GetParameter_ThucChayHopDongChiTietPRLog`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-09-08 15:26:38.333000
- **Ngày sửa cuối**: 2014-11-19 12:17:54.337000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[Gen_GetParameter_ThucChayHopDongChiTietPRLog] 	
As 	
Begin 	
Select 	
(Select Isnull(Max([ThoiGianLog]),'2010-01-01') from [dbo].[ThucChayHopDongChiTietPRLog] Where 1=1  and DeletedStatus <> 1) As 'NgaySua'	
End

```
