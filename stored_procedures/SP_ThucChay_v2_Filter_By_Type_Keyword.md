# Stored Procedure: `ThucChay_v2_Filter_By_Type_Keyword`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-05-13 16:55:37.100000
- **Ngày sửa cuối**: 2014-11-19 12:16:43.993000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@Count` | `int(4)` | No |
| `@TypeId` | `int(4)` | No |
| `@Keyword` | `nvarchar(8000)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<SonVM>
-- Create date: <13,05,2014>
-- Description:	<Description,,>

-- ThucChay_v2_Filter_By_Type_Keyword 10, 1, ''
-- ThucChay_v2_Filter_By_Type_Keyword 10, 2, ''
-- ThucChay_v2_Filter_By_Type_Keyword 50, 3, '7'
-- ThucChay_v2_Filter_By_Type_Keyword 10, 4, ''
-- ThucChay_v2_Filter_By_Type_Keyword 10, 5, 'BT'
-- ThucChay_v2_Filter_By_Type_Keyword 10, 6, N'Việt'
-- ThucChay_v2_Filter_By_Type_Keyword 10, 7, N'Điện tử'
-- ThucChay_v2_Filter_By_Type_Keyword 10, 8, N''
-- ThucChay_v2_Filter_By_Type_Keyword 10, 9, N''
-- =============================================
CREATE PROCEDURE [dbo].[ThucChay_v2_Filter_By_Type_Keyword]
	@Count   INT = 20,
	@TypeId  INT = 0,
	@Keyword NVARCHAR(4000) = NULL
AS
BEGIN	
	DECLARE @Sql     NVARCHAR(4000),
			@Params  NVARCHAR(4000)			
	
	SELECT @Sql = (SELECT CASE @TypeId
					-- Hình thức quảng cáo --
					WHEN 1
						THEN 'SELECT DISTINCT(DmLoaiREF) AS value, TenLoai AS [text] 
							  FROM HopDongChiTiet 
							  WHERE TenLoai <> '''' AND DeletedStatus = 0	
							  ORDER BY TenLoai'
						
					-- Sản phẩm --
					WHEN 2
						THEN 
							 'SELECT DISTINCT(DmSanPhamREF) AS value, TenSanPham AS [text] 
							  FROM HopDongChiTiet 
							  WHERE DeletedStatus = 0 
							  ORDER BY TenSanPham'
								
					-- Sản phẩm theo 'Hình thức quảng cáo' --
					WHEN 3
						THEN 
							 'SELECT DISTINCT(DmSanPhamREF) AS value, TenSanPham AS [text] 
							  FROM HopDongChiTiet
							  WHERE DmLoaiREF = ' + @Keyword + ' AND DeletedStatus = 0 
							  ORDER BY TenSanPham'		
					-- Banner (306: Facebook Ads, 423: Google Ads, 535: Chi phí quản lý) --
					WHEN 4
						THEN 'SELECT DISTINCT DmViTriREF AS value, TenViTri AS [text]
					   		  FROM ThucChayDaTinh 
							  WHERE DmSanPhamREF IN (306, 423, 535) AND DmViTriREF > 0
							  ORDER BY TenViTri'
					
					-- Hợp đồng --
					WHEN 5
						THEN 'SELECT TOP ' + CONVERT(VARCHAR(9), @Count) + ' HopDongID AS [value], SoHopDong AS [text]
							  FROM HopDong 
							  WHERE SoHopDong LIKE N''%' + @Keyword + '%'' AND DeletedStatus = 0																					  
							  ORDER BY SoHopDong'						
											
					-- Khách hàng --
					WHEN 6
						THEN 'SELECT TOP ' + CONVERT(VARCHAR(9), @Count) + ' KhachHangID AS [value], TenKhachHang AS [text] 
							  FROM KhachHangFull 
							  WHERE TenKhachHang LIKE N''%' + @Keyword + '%'' AND DeletedStatus = 0																					  
							  ORDER BY TenKhachHang'									
							  
					-- Ngành --
					WHEN 7
						THEN 'SELECT TOP ' + CONVERT(VARCHAR(9), @Count) + ' DmNghanhHangID AS [value], TenNghanhHang AS [text]
							  FROM DmNghanhHang 							  	
							  WHERE TenNghanhHang LIKE N''%' + @Keyword + '%'' AND DeletedStatus = 0																					  
							  ORDER BY TenNghanhHang'			
							  					
					-- Nhãn --
					WHEN 8
						THEN
							 ''		  							
							 
					-- Website - Sản phẩm --
					WHEN 9
						THEN
							 'SELECT DmWebsiteID AS [value], TenWebsite AS [text]
							  FROM rptDmWebsite 							  								  																				  
							  ORDER BY TenWebsite'		  							
				END)			
				
	SELECT @Params = '@Count INT, @Keyword NVARCHAR(4000)'
	
	PRINT (@Sql) 				
		
	EXEC sp_executesql @Sql, @Params, @Count, @Keyword 	
END

```
