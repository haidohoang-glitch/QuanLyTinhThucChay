# Stored Procedure: `Gen_GetParameter_DotChayHopDongChiTietLog`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-09-03 15:36:34.603000
- **Ngày sửa cuối**: 2014-11-19 12:16:51.337000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[Gen_GetParameter_DotChayHopDongChiTietLog] 	
As 	
Begin 	
Select 	
(Select Isnull(Max([ThoiGianLog]),'2010-01-01') from [dbo].[DotChayHopDongChiTietLog] Where 1=1  and DeletedStatus <> 1) As 'NgaySua'	
End

```
