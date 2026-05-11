# Stored Procedure: `SP_InsertOrUpdate_HopDongChiTietLog_FROM_TOOLCONTRACT`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-03-14 11:14:43.597000
- **Ngày sửa cuối**: 2025-03-13 11:44:53.470000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[SP_InsertOrUpdate_HopDongChiTietLog_FROM_TOOLCONTRACT] 	
AS
BEGIN
	DECLARE @MaxLogTime DATETIME
	DECLARE @SQL NVARCHAR(MAX),@server_id nvarchar(100) = '', @database nvarchar(100) = '', @daunhay nvarchar(10) = ''''

	SET @MaxLogTime =
	ISNULL((Select Isnull(Max(ThoiGianLog),'2010-01-01') from [dbo].[HopDongChiTietLog] Where 1=1  and DeletedStatus <> 1 AND GhiChu = 'SYN_TOOL_CONTRACT'),'2010-01-01')
	
	SET @server_id =
	ISNULL((SELECT TOP (1) (SERVER_ID) FROM dbo.Cau_hinh_linkserver WHERE deletedstatus = 0 AND GROUP_INPUT = N'CONTRACT' ORDER BY id),'')

	SET @database= 
	ISNULL((SELECT TOP (1) (DATA_NAME) FROM dbo.Cau_hinh_linkserver WHERE deletedstatus = 0 AND GROUP_INPUT = N'CONTRACT' ORDER BY id),'')

	CREATE TABLE #HopDongChiTietLog(
	[HopDongChiTietREF] [int] NOT NULL,
	[HopDongFK] [int] NOT NULL,
	[DanhSachNhanHangREF] [nvarchar](250) NULL,
	[NhanHang] [nvarchar](2000) NULL,
	[DmNhomNganhREF] [nvarchar](300) NULL,
	[TenNhomNganh] [nvarchar](2000) NULL,
	[DmLoaiREF] [bigint] NULL,
	[TenLoai] [nvarchar](500) NULL,
	[DmNhomWebsiteREF] [nvarchar](500) NULL,
	[TenNhomWebsite] [nvarchar](300) NULL,
	[DmWebsiteREF] [int] NULL,
	[TenWebsite] [nvarchar](200) NULL,
	[DmSanPhamREF] [int] NULL,
	[TenSanPham] [nvarchar](500) NULL,
	[DmLoaiBannerREF] [int] NULL,
	[TenLoaiBanner] [nvarchar](300) NULL,
	[DmChuyenMucREF] [int] NULL,
	[TenChuyenMuc] [nvarchar](500) NULL,
	[DmBannerREF] [int] NULL,
	[TenBanner] [nvarchar](500) NULL,
	[ThoiGian] [nvarchar](200) NULL,
	[SoLuong] [bigint] NULL,
	[DonViTinhREF] [int] NULL,
	[DonViTinh] [nvarchar](200) NULL,
	[DonGia] [float] NULL,
	[ChietKhau] [float] NULL,
	[GiamGia] [float] NULL,
	[TiLeTuVan] [float] NULL,
	[KhuyenMai] [nvarchar](200) NULL,
	[IsKhuyenMai] [int] NULL,
	[ChiPhiTuVan] [float] NULL,
	[ThanhTien] [float] NULL,
	[GhiChu] [nvarchar](max) NULL,
	[DmSanphamREF_old] [bigint] NULL,
	[TK_AdMarket] [nvarchar](1000) NULL,
	[TK_AdMarketID] [nvarchar](200) NULL,
	[SoLuongThucChay] [float] NULL,
	[ThanhTienThucChay] [float] NULL,
	[TrangThaiThucChay] [int] NULL,
	[ThoiGianBatDau] [datetime] NULL,
	[ThoiGianKetThuc] [datetime] NULL,
	[ThucChayDenNgay] [datetime] NULL,
	[ThoiGianLog] [datetime] NULL,
	[NguoiLog] [nvarchar](200) NULL,
	[LoaiLog] [int] NULL,
	[CreatedBy] [nvarchar](200) NULL,
	[CreatedAt] [datetime] NULL,
	[LastModifiedBy] [nvarchar](200) NULL,
	[LastModifiedAt] [datetime] NULL,
	[DeletedStatus] [int] NULL,
	[PrintStatus] [int] NULL,
	[RecordStatus] [int] NULL,
	[contract_detail_log_id] [bigint] NULL,
	Record_Status smallint
)
	 
	SET @SQL =
	'INSERT INTO #HopDongChiTietLog '
	SET @SQL +=
	'SELECT	 
		  ctdl.CONTRACT_DETAIL_ID HopDongChiTietID, 
          ctdl.CONTRACT_ID HopDongFK , 
		  ISNULL((SELECT 
				stuff(
				(
				SELECT cast(' + @daunhay +',' + @daunhay +' as varchar(max)) + CONVERT(NVARCHAR(50),U.BRAND_ID) FROM
				(SELECT DISTINCT U.BRAND_ID FROM  ' + @server_id + '.' + @database + '.dbo.CONTRACT_DETAIL_BRANDS U
					WHERE u.CONTRACT_DETAIL_ID = ctdl.CONTRACT_DETAIL_ID
					AND u.Deleted_Status = 0
				)U
				order by U.BRAND_ID
				for xml path('''') 
				), 1, 1, '''') AS ListBrandID
		  ),'''') DanhSachNhangHangREF,
		  '''' NhanHang,
		  ISNULL((SELECT --CHO NAY PHAI XEM LAI VI CACH LUU DU LIEU LOG, GIAI PHAP TAM THOI LA SU DUNG CONTRACT_DETAIL_BRAND
				stuff(
				(
				SELECT cast(' + @daunhay +',' + @daunhay +' as varchar(max)) + CONVERT(NVARCHAR(50),U.INDUSTRY_ID)
				FROM (SELECT DISTINCT U.INDUSTRY_ID FROM  ' + @server_id + '.' + @database + '.dbo.CONTRACT_DETAIL_BRANDS U
				WHERE u.CONTRACT_DETAIL_ID = ctdl.CONTRACT_DETAIL_ID
				AND u.Deleted_Status =0
				)U
				order by U.INDUSTRY_ID
				for xml path('''') 
				), 1, 1, '''') AS ListINDUSTRYID
		  ),'''') DmNhomNganhREF,
		  '''' TenNhomNganh,
          ctdl.PRODUCT_FORMALITY_ID DmLoaiREF , 
          '''' TenLoai,
		  '''' DmNhomwebsiteREF,
		  '''' TenNhomWebsite,
		  0 DmWebsiteREF,
		  '''' TenWebsite,
		  ctdl.PRODUCT_ID DmSanPhamREF , 
		  '''' TenSanPham,
		  0 DmLoaiBannerREF,
		  '''' TenLoaiBanner,
		  0 DmChuyenMucReF,
		  '''' TenChuyenMuc,
		  0 DmBannerREF,
		  '''' TenBanner,
		  '''' ThoiGian,
		  ctdl.QUANTITY SoLuong , 
          ctdl.PRODUCT_UNIT_ID DonViTInhREF , 
		  '''' DonViTinh,
          ctdl.PRICE DonGia , 
          ctdl.PERCENT_DISCOUNT_TOTAL ChietKhau , 
          ctdl.MONEY_DISCOUNT_TOTAL GiamGia , 
          ctdl.PERCENT_DISCOUNT_DIFFERENT TyleTuVan, 
		  ctdl.PROMOTION_COMMENT KhuyenMai , 
          ctdl.IS_PROMOTION IsKhuyenMai , 
          0 ChiPhiTuVan,
          ctdl.MONEY_TURNOVER Thanhtien , 
		  ' + @daunhay +'SYN_TOOL_CONTRACT' + @daunhay + ' GhiChu , 
          0 DmSanPHamOld,
		  ctdl.ADMARKET_USER_NAME TK_Admarket ,
		  ctdl.ADMARKET_USER_ID TK_AdMarket,
		  0 SoLuongThucChay,
		  ctdl.MONEY_REAL_RUNING ThanhTienThucChay , 
		  ctdl.IS_REAL_RUNING TrangThaiThucChay ,
          '''' ThoiGianBatDau,
		  '''' ThoiGianKetThuc,
          ctdl.DATE_REAL_RUNING ThucChayDenNgay ,
		  ctdl.LAST_MODIFIED_AT ThoiGianLog,
		  ctdl.LAST_MODIFIED_BY NguoiLog, 
		  ctdl.LOG_STATUS LoaiLog,
		  ctdl.CREATED_BY , 
          ctdl.CREATED_AT ,
          ctdl.LAST_MODIFIED_BY , 
          ctdl.LAST_MODIFIED_AT , 
          ctdl.DELETED_STATUS , 
		  0 PRINTSTATUS,
		  0 Recordstatus,
		  ctdl.ID contract_detail_log_id,
		  0 AS Record_Stauts
	FROM   ' + @server_id + '.' + @database + '.dbo.contract_detail_log ctdl
	WHERE  ctdl.LAST_MODIFIED_AT > ' + @daunhay + convert(nvarchar(23),@MaxLogTime,121)+ @daunhay+' '

	--PRINT @SQL
	EXEC(@SQL)

	--UPDATE TRANG THAI
	UPDATE L
	SET L.Record_Status = 1
	FROM #HopDongChiTietLog L 
	INNER JOIN dbo.HopDongChiTietLog h on L.contract_detail_log_id = h.contract_detail_log_id
	
	--INSERT INTO
	INSERT INTO dbo.HopDongChiTietLog
	SELECT [HopDongChiTietREF]
		  ,[HopDongFK]
		  ,[DanhSachNhanHangREF]
		  ,[NhanHang]
		  ,[DmNhomNganhREF]
		  ,[TenNhomNganh]
		  ,[DmLoaiREF]
		  ,[TenLoai]
		  ,[DmNhomWebsiteREF]
		  ,[TenNhomWebsite]
		  ,[DmWebsiteREF]
		  ,[TenWebsite]
		  ,[DmSanPhamREF]
		  ,[TenSanPham]
		  ,[DmLoaiBannerREF]
		  ,[TenLoaiBanner]
		  ,[DmChuyenMucREF]
		  ,[TenChuyenMuc]
		  ,[DmBannerREF]
		  ,[TenBanner]
		  ,[ThoiGian]
		  ,[SoLuong]
		  ,[DonViTinhREF]
		  ,[DonViTinh]
		  ,[DonGia]
		  ,[ChietKhau]
		  ,[GiamGia]
		  ,[TiLeTuVan]
		  ,[KhuyenMai]
		  ,[IsKhuyenMai]
		  ,[ChiPhiTuVan]
		  ,[ThanhTien]
		  ,[GhiChu]
		  ,[DmSanphamREF_old]
		  ,[TK_AdMarket]
		  ,[TK_AdMarketID]
		  ,[SoLuongThucChay]
		  ,[ThanhTienThucChay]
		  ,[TrangThaiThucChay]
		  ,[ThoiGianBatDau]
		  ,[ThoiGianKetThuc]
		  ,[ThucChayDenNgay]
		  ,[ThoiGianLog]
		  ,[NguoiLog]
		  ,[LoaiLog]
		  ,[CreatedBy]
		  ,[CreatedAt]
		  ,[LastModifiedBy]
		  ,[LastModifiedAt]
		  ,[DeletedStatus]
		  ,[PrintStatus]
		  ,[RecordStatus]
		  ,[contract_detail_log_id]
	  FROM #HopDongChiTietLog l
	  WHERE l.Record_Status = 0

	  DROP TABLE #HopDongChiTietLog
END

```
