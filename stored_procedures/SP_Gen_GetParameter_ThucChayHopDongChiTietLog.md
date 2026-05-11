# Stored Procedure: `Gen_GetParameter_ThucChayHopDongChiTietLog`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-09-08 15:11:20.063000
- **Ngày sửa cuối**: 2014-11-19 12:16:50.653000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[Gen_GetParameter_ThucChayHopDongChiTietLog] 	
As 	
Begin 	
Select 	
(Select Isnull(Max([ThoiGianLog]),'2010-01-01') from [dbo].[ThucChayHopDongChiTietLog] Where 1=1  and DeletedStatus <> 1) As 'NgaySua'	
End

```
