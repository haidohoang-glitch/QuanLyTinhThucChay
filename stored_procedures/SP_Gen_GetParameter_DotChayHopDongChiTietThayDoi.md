# Stored Procedure: `Gen_GetParameter_DotChayHopDongChiTietThayDoi`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-08-26 09:42:21.697000
- **Ngày sửa cuối**: 2014-11-19 12:16:51.303000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[Gen_GetParameter_DotChayHopDongChiTietThayDoi] 	
As 	
Begin 	
Select 	
(Select Isnull(Max([DotChayHopDongChiTietThayDoiID]),0) + 1 from [dbo].[DotChayHopDongChiTietThayDoi] Where 1=1  and DeletedStatus <> 1) As 'pid'	
End

```
